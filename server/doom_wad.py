DOOM_WAD = {
  "start": {
    "text": "UAC Base, Mars. Alarms blare. You wake up in your bunk, smell of ozone and burnt meat in the air. Your comm crackles: *Containment breach. Demons inbound.*",
    "options": [
      { "value": "grab-shotgun", "label": "Grab your shotgun" },
      { "value": "go-fist", "label": "Go in fists blazing" }
    ]
  },
  "grab-shotgun": {
    "text": "You rack your trusty shotgun. The hallway outside is slick with blood. A zombie soldier turns. You don't hesitate.",
    "options": [
      { "value": "blast-him", "label": "Blast him" },
      { "value": "run-past", "label": "Run past toward the armory" }
    ]
  },
  "go-fist": {
    "text": "No time for weapons? Bold. You punch through the first demon's face. It *loved* that. So did the imp behind it.",
    "options": [
      { "value": "rip-and-tear", "label": "RIP AND TEAR" },
      { "value": "retreat", "label": "Maybe this was a bad idea" }
    ]
  },
  "blast-him": {
    "text": "One shot, one mess. The armory is just ahead, sealed by a red keycard door. Something growls behind you.",
    "options": [
      { "value": "search-body", "label": "Search the corpse for keycard" },
      { "value": "face-growl", "label": "Turn around, face the growl" }
    ]
  },
  "run-past": {
    "text": "You sprint past the zombie, but trip over a dismembered leg. You look up — **Baron of Hell**. Oops.",
    "options": [
      { "value": "shoot-up", "label": "Blast him from the floor" },
      { "value": "scream", "label": "Scream like a mortal" }
    ]
  },
  "rip-and-tear": {
    "text": "The imp is shredded. You feel the rage—primal, beautiful. A rocket launcher lies in the next room, glowing.",
    "options": [
      { "value": "take-rocket", "label": "Take the rocket launcher" },
      { "value": "throw-imp", "label": "Throw the imp’s head like a bowling ball" }
    ]
  },
  "retreat": {
    "highlight": "error",
    "text": "You flee back to the bunk, only to find a **cacodemon** munching your pillow. It turns. You die tired.",
    "options": []
  },
  "search-body": {
    "text": "Red keycard acquired. Growl intensifies. You spin around and see... **Cyberdemon**. Why always Cyberdemon?",
    "options": [
      { "value": "run-to-armory", "label": "Open armory and pray" },
      { "value": "charge-it", "label": "CHAAAAARGE!" }
    ]
  },
  "face-growl": {
    "text": "It's a pinky. It charges. You sidestep, it crashes into a pipe and explodes. Messy. Satisfying.",
    "options": [
      { "value": "search-body", "label": "Search zombie corpse for keycard" }
    ]
  },
  "shoot-up": {
    "text": "**Boom!** Right in the horned face. Baron falls, but not before leaving scorch marks on your armor.",
    "options": [
      { "value": "continue", "label": "Stagger onward, badass" }
    ]
  },
  "scream": {
    "highlight": "error",
    "text": "You scream. The Baron laughs. Then it turns you into jam. Game over, civilian.",
    "options": []
  },
  "take-rocket": {
    "text": "Rocket launcher obtained. Ammo? Just enough for *one* heroic overkill. What will it be?",
    "options": [
      { "value": "blow-door", "label": "Blow open a shortcut" },
      { "value": "save-it", "label": "Save it for the Cyberdemon" }
    ]
  },
  "throw-imp": {
    "text": "Strike! The imp's head knocks down a zombie, who trips and falls onto a chainsaw. It revs up. Ooooh.",
    "options": [
      { "value": "grab-chainsaw", "label": "Grab the chainsaw" }
    ]
  },
  "run-to-armory": {
    "text": "The armory slides open. Inside: **BFG9000**. You grin.",
    "options": [
      { "value": "use-bfg", "label": "Use the BFG!" }
    ]
  },
  "charge-it": {
    "text": "You charge the **Cyberdemon** and uppercut it with your shotgun. It’s stunned. You’re a god now.",
    "options": [
      { "value": "grab-bfg", "label": "Grab BFG while it’s down" }
    ]
  },
  "continue": {
    "highlight": "info",
    "text": "You live. For now. You’ve got the keycard, a shotgun, and a lot of rage. Time to clear this base.",
    "options": []
  },
  "blow-door": {
    "text": "**BOOM**. You shortcut right to the portal room. One portal to Earth, one to Hell. Choose wisely.",
    "options": [
      { "value": "to-earth", "label": "Escape to Earth" },
      { "value": "to-hell", "label": "Take the fight to Hell" }
    ]
  },
  "save-it": {
    "highlight": "info",
    "text": "You save your shot. Smart. The **Cyberdemon** appears. You fire. Everything goes white. Victory.",
    "options": []
  },
  "grab-chainsaw": {
    "text": "The chainsaw hums like a lullaby. You’re now 30% more terrifying.",
    "options": [
      { "value": "to-hell", "label": "Chainsaw your way to Hell" }
    ]
  },
  "use-bfg": {
    "highlight": "info",
    "text": "The BFG hums... then obliterates everything in a green flash. No more demons. Just smoke and silence.",
    "options": []
  },
  "grab-bfg": {
    "highlight": "info",
    "text": "You grab the BFG and finish the job. Cyberdemon down. Mars is safe—for now.",
    "options": []
  },
  "to-earth": {
    "highlight": "info",
    "text": "You step through the portal and return to Earth. You’re safe. But Hell remembers you.",
    "options": []
  },
  "to-hell": {
    "highlight": "info",
    "text": "You enter the Hell portal, chainsaw roaring. Time to rip and tear... until it is done.",
    "options": []
  }
}

