# Topic 5: Applications I — Computer Vision, Cinema, Activity Recognition, Captioning, Object Detection, Self-Driving Cars

Source: Lecture 1, slides 19–28 (Applications: Computer vision; 4D / 7D / 9D cinema; Activity Recognition; Image Captioning ×2; Object Identification; Automated Car).

---

## 1) Technical Explanation

| Slide | Application | What the slide says / shows |
|---|---|---|
| 19 | **Computer vision** | 2D→3D conversion, street-view generation, image classification, image segmentation (picture: a 2D football photo converted to 3D) |
| 20–22 | **4D / 7D / 9D cinema** | 4D = 3D movie + dynamic seat system (simulates the film's motion); 7D = an upgrade of 3D/4D/5D/6D that adds interactivity (and plays all lower formats); 9D = 3D + dynamic seat + environment effects + interactive + Virtual Reality. Comparison table: 4D ✓ 3D movie, ✓ dynamic seat; 5D adds the environment system; 7D adds the interactive system; 9D adds VR. Source: stekiamusement.com |
| 23 | **Activity recognition** | Recognise walking, running, cooking, … from a still image or video (pictures: pose skeletons fitted to people shaking hands, silhouettes of many poses) |
| 24–25 | **Image captioning** | Automatic caption generation for a given image. Slide 25 shows the same 12 images colour-coded by caption quality: *describes without errors*, *describes with minor errors*, *somewhat related to the image*, *unrelated to the image* |
| 26 | **Object identification** | Find objects in still images or video streams (bounding boxes around people/horse, and around bottles) |
| 27 | **Automated car** | Self-driving car |

**Key idea.** Every row is a *perception* task — the "Category B" problems of [[02_Problem_Space_Easy_for_Humans_vs_Easy_for_Computers]]. Classification (what is it?), detection (where is it?), segmentation (which pixels?), captioning (describe it in words) are different output formats on the same input, an image.

**Flag — the cinema slides.** Slides 20–22 are about *entertainment venues* (4D/7D/9D theatres), taken from a cinema-equipment vendor's article. Nothing on the slides says deep learning is used inside them; they appear to be there as an "application area" illustration of immersive 3-D/VR media. They are noted here as stated, without claiming a DL mechanism the slides do not give.

**Caption-quality slide (25).** It is a useful honesty check: even good captioning systems fail on some images — the red column shows captions like "A refrigerator filled with lots of food and drinks" for a road-sign photo, i.e. the model describes what its learned statistics suggest rather than what is truly there.

---

## 2) Simple English Explanation

These slides show things computers do with pictures and video:

- turn a flat photo into a 3-D one, build street-view maps, say what a picture shows, and mark exactly which pixels belong to which object;
- recognise what a person is doing (walking, running, cooking);
- write a sentence describing a photo — and the slide even shows which sentences were right, nearly right, and totally wrong;
- find and box objects like people, horses and bottles;
- drive a car by themselves.

Three slides also talk about 4D/7D/9D cinemas: ordinary 3-D movies plus moving seats, wind/water effects, interactivity and VR. Those are about entertainment rides, not about learning.

---

## 3) Hinglish Explanation (Beginner-Friendly)

Ye slides dikhati hain ki computer pictures aur video ke saath kya-kya karta hai:

- flat photo ko 3-D bana dena, street-view maps banana, bata dena ki picture mein kya hai, aur exactly kaun se pixels kis object ke hain;
- pehchanna ki insaan kya kar raha hai (chalna, daudna, khana banana);
- photo ke liye ek sentence likhna — aur slide ye bhi dikhati hai ki kaunse sentences sahi the, lagbhag sahi the, aur bilkul galat the;
- people, ghode aur bottles jaise objects dhoondh kar unke around box banana;
- gaadi khud chalana.

Teen slides 4D/7D/9D cinema ke baare mein bhi hain: normal 3-D movie ke saath hilti seats, hawa/paani ke effects, interactivity aur VR. Ye entertainment ride ke baare mein hain, learning ke baare mein nahi.
