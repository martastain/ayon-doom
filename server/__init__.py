from ayon_server.actions import (
    ActionExecutor,
    ExecuteResponseModel,
    SimpleActionManifest,
)

from ayon_server.actions.context import ActionContext
from ayon_server.addons import BaseServerAddon
from ayon_server.entities import UserEntity
from ayon_server.exceptions import NotImplementedException
from ayon_server.forms import SimpleForm
from ayon_server.utils import hash_data

from .doom_wad import DOOM_WAD


ENTRYPOINT = SimpleActionManifest(
    identifier="doom-run-doom",
    label="DOOM",
    category="server",
    order=99,
    icon={"type": "url", "url": "https://blue.imm.cz/doom.png"},
    entity_type="folder",
    entity_subtypes=None,
    allow_multiselection=False,
    config_fields=SimpleForm().select(
        "difficulty",
        label="Difficulty",
        value="easy",  # default value
        options=[
            {"value": "baby", "label": "I'm too young to die!"},
            {"value": "easy", "label": "Hey, not too rough!"},
            {"value": "medium", "label": "Hurt me plenty!"},
            {"value": "hard", "label": "Ultra-Violence!"},
            {"value": "nightmare", "label": "Nightmare!"},
        ],
    ),
)


class DoomAddon(BaseServerAddon):
    addon_type = "server"

    async def get_simple_actions(
        self,
        project_name: str | None = None,
        variant: str = "production",
    ) -> list[SimpleActionManifest]:
        """Return a list of simple actions provided by the addon"""

        _ = project_name  # Unused
        _ = variant  # Unused
        return [ENTRYPOINT]

    async def execute_action(
        self,
        executor: ActionExecutor,
    ) -> ExecuteResponseModel:
        """Execute an action provided by the addon"""

        if executor.identifier != "doom-run-doom":
            # We only expose dum-run-doom action
            # So we raise error if the action is not found
            raise NotImplementedException("Invalid action identifier")

        # Get the action config
        config = await executor.get_action_config()

        ended = False

        if form_data := executor.context.form_data:
            location = executor.context.form_data.get("location", "start")
            ended = executor.context.form_data.get("ended", False)

            if config.get("difficulty") == "nightmare" and location != "start":
                # Nightmare difficulty is not even remotely fair.
                # We kill you as soon you leave the starting location
                return await executor.get_server_action_response(
                    message="You died",
                    form=SimpleForm()
                    .hidden("ended", True)
                    .label(
                        "A wild spider mastermind appeared and killed you. "
                        "This difficulty level is not fair at all.",
                        highlight="error",
                    ),
                )

        if ended:
            message = "The game has ended."
            return await executor.get_server_action_response(message=message)

        if not form_data:
            # New game.
            location = "start"

        loc_data = DOOM_WAD.get(location)
        if not loc_data:
            raise ValueError(f"Invalid location: {location}")

        form = SimpleForm()
        form.label(loc_data["text"], highlight=loc_data.get("highlight"))
        if options := loc_data.get("options", []):
            form.select(
                "location",
                label="What would you do?",
                options=loc_data["options"],
                value=options[0]["value"],
            )
        else:
            # No options, so the game is over
            # Next time user submits the form,
            # We just show the game over message
            # and finaize the action
            form.hidden("ended", True)

        # When we're returning a form, message is used as the form header
        # Otherwise, message is just toasted
        return await executor.get_server_action_response(message="DOOM", form=form)

    async def create_config_hash(
        self,
        identifier: str,
        context: ActionContext,
        user: UserEntity,
        variant: str,
    ) -> str:
        """Create a hash for action config store"""

        # Override the default function for creating config hash
        # Normally the hash is created from the action identifier,
        # project name and user name

        # In this case we include context.entity_subtypes as well,
        # so every folder type has a different difficulty level

        hash_content = [
            user.name,
            identifier,
            context.project_name,
            context.entity_subtypes,
        ]
        return hash_data(hash_content)
