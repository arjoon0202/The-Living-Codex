# Phase 3: Tidus Full Rebuild

> **Status: Archived** — Completed March 13, 2026. Tidus fully rebuilt as polar bear–sea otter hybrid with Sango Sango no Mi shell shovel, Yuki Yuki no Mi + Kawa Kawa no Mi hidden fruits, sea curse immunity. Superseded by live `src/` content.

## Scope
Complete character rebuild for Tidus (formerly Tethys): rewrite companion panel, new backstory, new Fishman DNA (clownfish + fancy goldfish), new Fishman Karate, new martial art category (Sub-Arctic Art), new Conqueror's Haki philosophy (The Fluffy Doctrine), new Rokushiki, shell shovel weapon with Zoan Reef-Reef Fruit, snow/ice production, remove ALL Green Blood content. This is the most extensive single-character rewrite.

## CRITICAL SAFETY RULES
- **No content deletion** — every technique section must continue to exist (rewritten or replaced, not removed)
- **Read `MERIDIAN_CREW_REFERENCE.md` before touching any character content** — Tidus is MALE (he/him), Claude uses NO gendered pronouns
- **Never edit `dist/hive_codex.html` directly** — edit source files in `src/tabs/` and `src/tabs/panels/`
- **Never read `.b64` image files directly**
- **Run `python build.py` after all changes and verify clean compilation**
- **Hawaiian/Polynesian move naming convention is PRESERVED** — Tidus' techniques use Hawaiian/Polynesian names
- **Never call bio-film "mucus"** — use "protective film," "bio-film membrane," "film coating," etc.
- **This is a retcon of love** — Tidus should feel like he was ALWAYS a polar bear-otter

## Pre-Phase Checklist
- [ ] Phases 1-2 completed (all "Tethys" → "Tidus" done, species updated)
- [ ] Read `MERIDIAN_CREW_REFERENCE.md` for pronoun reference
- [ ] Read `CLAUDE.md` for panel file map

## Key Files to Edit
| Content | File |
|---------|------|
| Tidus companion profile | `src/tabs/panels/06-companions-tidus.html` (renamed from tethys in Phase 1) |
| Fighting Styles — Tidus | `src/tabs/panels/07-fighting-petal-tethys.html` (check if renamed) |
| Haki Transcendence — Tidus | `src/tabs/11-haki-transcendence.html` |
| Auxiliary Protocols — Tidus | `src/tabs/09-auxiliary-protocols.html` |
| Armory — Weapons | `src/tabs/panels/14-armory-weapons.html` |
| Extended Family — Copplings | `src/tabs/panels/10-family-gearlings-copplings.html` |
| Arsenal — Signature Moves (Tidus tags) | `src/tabs/panels/04-arsenal-moves.html` |
| CSS | `src/head/styles.css` |
| Content Reference | `CODEX_CONTENT_REFERENCE.md` |

---

## Step 1: Rewrite Companion Panel — Full Profile

### File: `src/tabs/panels/06-companions-tidus.html`

This is the master character file. COMPLETE rewrite of species, appearance, personality expressions, backstory, and abilities.

### Appearance (rewrite from scratch):
- **Species**: Polar Bear–Sea Otter Hybrid (Vegapunk Experiment #[number from existing lore] + Fishman DNA + Pacifista Modifications)
- **Body**: Adorably chubby. Dense polar bear muscle hidden under incredibly soft white/cream fur with sea otter water-repellent density. Round belly. Slightly oversized paws. He looks like a living teddy bear
- **Eyes**: Blue, warm, gentle. When he's focused on engineering, they sharpen with frightening intelligence
- **Fur**: White/cream polar bear base with the impossibly dense, water-repellent quality of sea otter fur. When wet, his fur has an iridescent sheen from his bio-film (clownfish DNA). When dry, he's the fluffiest thing on the Grand Line
- **Paws**: Slightly webbed (otter influence), with the heavy-set structure of a polar bear. Capable of incredible precision despite their size — he builds microengineering marvels with these paws
- **Tail**: More otter than bear — flat, broad, useful for swimming and balance. Also makes an excellent rudder when he's building underwater
- **Size**: Large enough to be imposing, adorable enough to be hugged. When he stands on hind legs, he's taller than most humans. When he sits down, children want to climb on him
- **Pacifista modifications**: Internal reinforcement — enhanced skeletal structure, embedded power systems, internal weapon hardpoints. NOT visually obvious from outside. Another reason Vegapunk classified him as "failed" — the weapons are there but he refuses to use most of them offensively

### Personality expressions (SAME personality, new body language):
- **Contentment**: Chuffs softly, rolls onto his back (otter grooming behavior), closes his eyes
- **Excitement (engineering)**: Paws patter rapidly on whatever surface he's near (bear excitement behavior). His tail smacks the ground
- **Protective mode**: Rises to full height on hind legs (polar bear threat display but from a gentle creature), low rumbling purr, fur bristles slightly
- **Alarm**: Sharp bark. Teeth bared (polar bear has formidable teeth). Immediately positions himself between threat and whoever needs protecting
- **Happiness**: Cooing chirp (sea otter influence). Sometimes he floats on his back in water and chirps — this is his most peaceful state
- **Apology**: Ducks his head, covers his muzzle with both paws (otter face-covering), makes small whimpering sounds. He does this after hitting opponents

### Backstory (COMPLETE REWORK):
**Remove entirely:**
- The ceramic shard in laboratory aquarium depicting Tethys/Titan goddess
- Any reference to "Tethys" as a mythological name choice
- The laboratory aquarium as name origin

**New backstory:**
- Vegapunk's lab, experiment intended to create the ultimate aquatic predator hybrid
- The polar bear genes were chosen for Arctic survival, raw power, apex predator status
- The sea otter genes were chosen for aquatic dexterity, tool use, fur insulation
- The Fishman DNA (clownfish + fancy goldfish) was chosen for underwater adaptation
- The Pacifista modifications were standard for combat enhancement
- What they got: an overwhelmingly adorable creature who preferred building blocks to battle drills, who apologized to test dummies after hitting them, and who once spent three hours repairing a laboratory door he'd accidentally broken during a strength test
- The researchers classified him as a failure. The creature they wanted to be terrifying was, instead, terrifyingly kind

**Name origin (the beating heart of this retcon):**
As a baby in Vegapunk's lab, Tidus could hear the tides through the walls. The laboratory was coastal — built into cliffs above the sea. At night, when the machines quieted and the researchers went home, the rhythmic pulse of ocean against stone was the only sound that wasn't clinical. It was the only thing in his world that felt like it was there FOR him, not STUDYING him.

When he first tried to speak — early, before the researchers expected language — he attempted to say "tides." The word that meant safety. Comfort. The thing that never stopped coming back, no matter how bad the day had been.

What came out, in his small, earnest voice, was: "Tidus."

He never corrected it. He didn't know it was wrong. The researchers logged it as a designation error — "Subject T-[number] self-identifies as 'Tidus,' catalogued as speech development anomaly." They never realized it was a love letter to the only friend he had.

### Fishman DNA — Clownfish + Fancy Goldfish:
**Remove entirely:**
- Mantis shrimp DNA
- Pistol shrimp DNA
- Cavitation crack/snap (this was the mantis/pistol shrimp combat sound)

**New Fishman DNA:**

**Clownfish (Amphiprioninae):**
- **Protective Bio-Film Coating**: Produces a film membrane that grants immunity to contact toxins, acids, and chemical attacks. This is the clownfish's real-world superpower — they produce a mucus coating (WE CALL IT "BIO-FILM" or "PROTECTIVE FILM," NEVER "mucus") that makes them immune to anemone stings
- **Extendable Protection**: Tidus can extend this bio-film to coat allies — creating incredible synergy with Rime's acidic vapor (Tidus is naturally immune to it and can protect others walking through acid clouds)
- **Territorial Instinct**: Despite being gentle, clownfish are fiercely territorial. Tidus' protective instinct is literally in his DNA. He doesn't get aggressive for himself — he gets aggressive for everyone he considers family
- **Symbiotic Nature**: Clownfish live in mutual protection relationships. Tidus doesn't just protect — he enables. His presence makes everyone around him stronger

**Fancy Goldfish (Ranchu/Oranda type):**
- **Adorable Resilience**: Goldfish survive conditions that kill most fish — temperature extremes, low oxygen, poor water quality. The goldfish DNA is why Tidus is indestructible despite looking like a plush toy
- **Round Body Enhancement**: The "chubby goldfish" DNA contributes to his adorable roundness
- **Bio-Film Production**: Enhanced bio-film output (goldfish also produce protective slime coating — again, we call it "bio-film")
- **Deceptive Softness**: Looks harmless, survives everything. Peak Tidus energy

### Combat Sound Signature:
**Remove**: Cavitation crack (that was mantis/pistol shrimp)
**New**: A deep resonant POP — the sound of film-coated water bursting under enormous pressure. Think of a giant bubble popping with concussive force. When the crew hears that sound, they know Tidus just hit something with intent.

---

## Step 2: Fishman Karate — Complete Rewrite

### File: `07-fighting-petal-tethys.html` (or wherever Tidus' fighting style is documented)

The existing Fishman Karate is written for crab anatomy (claw-palm strikes, lateral movement, hydraulic charges). COMPLETE REWRITE for polar bear-otter body.

### New Fishman Karate Core:
Tidus' Fishman Karate is built around **film-membrane water manipulation** — thick, viscous water constructs that aren't just walls but sticky, clinging, shock-absorbing membranes.

**Primary striking technique** (replacing Claw Palm — Depth Charge):
**Paw-Clap Shockwave** — Tidus claps his heavy polar bear paws together, compressing film-coated water between them. The resulting pop sends a viscous shockwave that clings to whatever it hits. Unlike a sharp impact that pushes through, this shockwave WRAPS around the target and continues delivering internal pressure damage after the initial hit. Less sharp crack, more deep resonant pop.

**Key principles:**
- Water manipulation through bio-film medium — his water constructs have TEXTURE. They're sticky, elastic, iridescent
- Film-coated water bubbles that are incredibly durable (bio-film + light = rainbow shimmer)
- His blocks create sticky water barriers that grab and slow incoming attacks
- His strikes deliver force through a film-water medium that clings to the target
- Underwater, he's even more devastating — polar bear swimming power + otter agility + Fishman water control

### Named techniques (preserve Hawaiian/Polynesian naming):
Rewrite all existing Tidus Fishman Karate techniques. Each technique should:
- Have a Hawaiian/Polynesian name (matching existing convention)
- Describe the new polar bear-otter execution
- Reference bio-film water mechanics
- Sound devastating AND adorable simultaneously

---

## Step 3: Sub-Arctic Art (Replacing Crustacean Art)

### Rename throughout all files:
- "Crustacean Art" (甲殻術 / Kōkaku-jutsu) → **"Sub-Arctic Art"** (亜北極術 / A-Hokkyoku-jutsu)
  - Or find a better Japanese rendering. Consider: 極地術 (Kyokuchi-jutsu, "Polar Art") or 氷原術 (Hyōgen-jutsu, "Ice Field Art")
  - The name should evoke polar/Arctic themes

### Rewrite all Sub-Arctic Art techniques:
Same defensive identity — he hunkers down, becomes immovable, refuses to let anything through. But instead of chitin and shell:
- **Dense polar bear-otter fur** (naturally insulating, shock-absorbing)
- **Thick muscle** (polar bears have enormous muscle mass under their fur)
- **Pacifista internal reinforcement** (embedded titanium/alloy skeletal reinforcement)
- **Bio-film coating** (adds a slick, impact-dispersing layer)
- **Ryou compression** (channeled through all of the above)

The image: A polar bear doesn't scuttle behind a shell — it PLANTS ITSELF and becomes a wall of fur and muscle and unbreakable will. A sea otter wraps itself around what it loves and refuses to let go.

---

## Step 4: The Fluffy Doctrine (Replacing The Crustacean Doctrine)

### Conqueror's Haki Philosophy:
Same power level (Supreme Ruler-tier), same philosophy (absolute protection), new physical language.

**Rename**: "The Crustacean Doctrine" → **"The Fluffy Doctrine"**

**Rewrite the philosophy:**
- The Crustacean Doctrine was about an impenetrable shell. The Fluffy Doctrine is about an inescapable embrace
- Tidus' Conqueror's Haki doesn't project outward as a wall — it envelops. It wraps around everything he's chosen to protect like a polar bear curling around its cubs
- His sovereign will says: "Nothing touches what I love. Not because I am hard. Because I am WARM, and the warmth goes all the way down, and there is more warmth than you have cold."

**Technique rename**: "Carapace of the Sovereign" → **"Embrace of the Sovereign"**
- Description: Tidus hunkers low, wraps his arms around himself (the way bears protect their vital organs), fur bristling with Haki, bio-film barrier enveloping him, and becomes an immovable fortress of fluff and sovereign will. Anyone trying to reach what's behind him has to go through the softest, most indestructible wall in the New World.

---

## Step 5: Rokushiki Adaptation

### Rewrite for polar bear-otter body:

- **Tekkai**: Devastating given his natural bulk + dense fur + Pacifista reinforcement + bio-film coating. Combined with Conqueror's Haki, he becomes virtually impenetrable. The most natural Rokushiki for Tidus — he was BUILT to take hits.
- **Geppo**: Powerful hind-leg bursts (bears have incredible leg strength). Less rapid than Rime's but each air-step covers more distance and hits harder. The air beneath him compresses visibly. His Geppo looks like a polar bear bounding through the sky.
- **Soru**: Forward charges rather than lateral scuttling. A polar bear at Soru-speed is a freight train of fluff. The ground cracks. The air displaces. And then the softest possible collision.
- **Shigan**: Paw-thrust variant. Less pointed than finger-pistol (bears have blunt claws), more about channeling massive force through a single point. Also: his bite. Polar bear jaw strength is extraordinary.
- **Rankyaku**: Less conventional. Tidus' Rankyaku comes from tail sweeps (otter tail is flat and powerful) or massive paw swipes that compress air into cutting waves. The waves are thick and visible — like water blades.
- **Kami-e**: The most surprising one. Tidus looks like he shouldn't be able to dodge anything. But sea otters are INCREDIBLY fluid in water, and that translates to a deceptive body fluidity on land. His Kami-e is a gentle, swaying evasion — opponents' attacks slide off him like he's made of water.

---

## Step 6: Shell Shovel Weapon + Zoan Reef-Reef Fruit

### New weapon section:
Tidus carries a **shell-shaped shovel/staff** — a blue staff topped with an iridescent shell fan. This is both his building tool and his weapon.

**The weapon has eaten the Sango Sango no Mi — Reef-Reef Fruit:**
- Reimagined as a **Zoan-type Devil Fruit** (corals are living creatures — colonial animals — so this is a Zoan that allows the weapon to "become" a living coral reef entity)
- NOT Paramecia. NOT Green Blood extract. The fruit was fed to the weapon directly (like Spandam's Funkfreed or Lassoo)
- The weapon can transform: the shell fan can grow, branch, and reshape into coral structures. It can extend coral walls, create barriers, grow reef architecture
- In full transformation, the staff becomes a living reef creature that Tidus wields/rides/directs

**Seawater protection:**
The weapon has standard Devil Fruit weakness to seawater. Tidus protects it using:
- His powerful Haki coating
- Fishman Karate water manipulation — he maintains a bio-film barrier around the weapon when submerged, shielding it from direct seawater contact
- This requires active concentration, adding a tactical dimension (he can't be reckless underwater with the weapon out)

**Coral techniques (reflavoured):**
All existing coral generation now comes FROM THE WEAPON, not from Tidus' body.
- The aesthetic is similar — living coral, bioluminescence, architectural precision
- But the source is different: he channels through the shell shovel
- Coral Art techniques (Reef Crown, Tidal Garden, etc.) stay but are rewritten to show coral growing from the weapon

### Where to add:
- Companion profile: Equipment section
- Armory weapons panel (`14-armory-weapons.html`): Full weapon entry with Zoan details
- Fighting Style: Weapon combat section

---

## Step 7: Remove ALL Green Blood Content

### CRITICAL — Complete removal:
Search ALL files for:
- "Green Blood" → REMOVE all references
- "green blood" → REMOVE
- "partial extract" → REMOVE in Tidus context
- "sub-threshold for DF weakness cascade" → REMOVE
- "Sango Sango no Mi" as Paramecia → CHANGE to Zoan (weapon's fruit)
- Vegapunk's Green Blood experiments on Tidus → REMOVE

The narrative is now:
- Tidus has NO Devil Fruit power himself
- The coral power comes from the WEAPON'S Zoan fruit (Sango Sango no Mi)
- His bio-film is from his clownfish Fishman DNA, NOT from Green Blood

### Files likely containing Green Blood references:
- `06-companions-tidus.html` — main profile
- `07-fighting-petal-tethys.html` — fighting style
- `27-devil-fruit-awakening.html` or its sub-panels — awakening section
- Various mission log and combo attack references
- `CODEX_CONTENT_REFERENCE.md`

---

## Step 8: New Ability — Powdered Snow/Ice Production

### Core concept:
Tidus' polar bear genes allow him to produce powdered snow and ice. This takes over the cold element from Rime.

**Details:**
- Natural biological ability from polar bear heritage, NOT a Devil Fruit power
- He can generate ice structures, snow fields, and freezing environments
- The ice is distinctly his — it has a slightly blue-white quality with the iridescent sheen of his bio-film
- Combined with his coral weapon, he can create frozen reef structures — coral formations encased in or growing through ice
- In the Guanyin attack, Tidus now provides the ice/cold element (the frozen landscape, the temperature drop, the frozen constructs)

### Integration:
- Add to companion profile abilities section
- Add to fighting style
- Mention in combo attack contexts where cold was previously Rime's contribution

---

## Step 9: Build & Verify

1. Run `python build.py`
2. Verify clean compilation (no errors)
3. Search the built output for orphaned references:
   - `grep -i "crustacean" dist/hive_codex.html` — should be ZERO
   - `grep -i "carapace" dist/hive_codex.html` — should be ZERO
   - `grep -i "chitin" dist/hive_codex.html` — should be ZERO
   - `grep -i "Green Blood" dist/hive_codex.html` — should be ZERO
   - `grep -i "mantis shrimp\|pistol shrimp" dist/hive_codex.html` — should be ZERO
   - `grep -i "scuttling\|scuttle" dist/hive_codex.html` — should be ZERO in Tidus context
   - `grep -i "claw" dist/hive_codex.html` — review all hits, should be ZERO in Tidus context
   - `grep -i "ceramic shard\|ceramic fragment" dist/hive_codex.html` — should be ZERO
   - `grep -i "mucus" dist/hive_codex.html` — should be ZERO (use "film" terminology)
   - `grep -i "cavitation" dist/hive_codex.html` — should be ZERO
4. Verify div balance

---

## Phase 3 Completion Checklist
- [ ] Tidus companion panel completely rewritten (appearance, personality, backstory)
- [ ] New name origin story (baby voice "tides") — old ceramic shard story removed
- [ ] Fishman DNA rewritten: clownfish + fancy goldfish (bio-film mechanics)
- [ ] ALL mantis shrimp / pistol shrimp references removed
- [ ] Fishman Karate completely rewritten for mammalian body with film-membrane water manipulation
- [ ] "Crustacean Art" → "Sub-Arctic Art" globally
- [ ] "The Crustacean Doctrine" → "The Fluffy Doctrine"
- [ ] "Carapace of the Sovereign" → "Embrace of the Sovereign"
- [ ] Rokushiki adaptation rewritten for polar bear-otter body
- [ ] Shell shovel weapon added with Zoan Reef-Reef Fruit
- [ ] ALL Green Blood content removed
- [ ] Sango Sango no Mi changed from Paramecia to Zoan (weapon's fruit)
- [ ] Snow/ice production ability added (polar bear heritage)
- [ ] New combat sound signature (deep resonant pop, not cavitation crack)
- [ ] Vocalizations updated (chuffing, purring, barking, chirping — no clicking)
- [ ] All anatomy references updated (paws not claws, fur not carapace, etc.)
- [ ] Hawaiian/Polynesian naming convention preserved
- [ ] "mucus" never appears — only "bio-film" / "protective film" / "film coating"
- [ ] CODEX_CONTENT_REFERENCE.md mirrored
- [ ] `python build.py` runs clean
- [ ] Div balance verified
- [ ] The voice is right — Tidus still sounds warm, gentle, brilliant, funny
