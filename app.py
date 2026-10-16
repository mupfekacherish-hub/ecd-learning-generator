
import os
from datetime import datetime

import streamlit as st
from supabase import create_client

set_page_config()
    page_title="ECD Learn & Grow",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Connect to the Supabase database
supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"],
)

# -----------------------------
# ECD LEARNING CONTENT
# Picture-first activities are used for younger learners.
# -----------------------------


    page_title="ECD Learn & Grow",
    page_icon="🌈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# ECD LEARNING CONTENT
# Picture-first activities are used for younger learners.
# -----------------------------
AREAS = {
    "Mathematics": {
        "icon": "🔢",
        "topics": {
            "Counting and number recognition": [
                {"prompt": "Touch the group with THREE apples.", "choices": [("🍎", "one apple"), ("🍎 🍎 🍎", "three apples"), ("🍎 🍎", "two apples")], "answer": "three apples", "objective": "Count objects and match a quantity."},
                {"prompt": "Which picture shows ONE ball?", "choices": [("⚽ ⚽", "two balls"), ("⚽", "one ball"), ("⚽ ⚽ ⚽", "three balls")], "answer": "one ball", "objective": "Recognise a quantity of one."},
            ],
            "Shapes and patterns": [
                {"prompt": "Touch the circle.", "choices": [("🔺", "triangle"), ("🟦", "square"), ("⚪", "circle")], "answer": "circle", "objective": "Recognise basic shapes."},
                {"prompt": "What comes next? 🔴 🔵 🔴 🔵 ...", "choices": [("🔴", "red"), ("🔵", "blue"), ("🟢", "green")], "answer": "red", "objective": "Continue a simple pattern."},
            ],
            "Sorting and comparing": [
                {"prompt": "Touch the BIG animal.", "choices": [("🐘", "big elephant"), ("🐜", "small ant"), ("🐁", "small mouse")], "answer": "big elephant", "objective": "Compare sizes."},
            ],
            "Addition and subtraction": [
                {"prompt": "You have one banana. You get one more. How many bananas?", "choices": [("🍌", "one banana"), ("🍌🍌", "two bananas"), ("🍌🍌🍌", "three bananas")], "answer": "two bananas", "objective": "Explore joining groups using pictures."},
            ],
            "Measurement": [
                {"prompt": "Touch the FULL cup.", "choices": [("🥛", "full cup"), ("🥤", "empty cup"), ("🫗", "spilled drink")], "answer": "full cup", "objective": "Compare full and empty."},
            ],
        },
    },
    "Shona": {
        "icon": "🗣️",
        "topics": {
            "Mazita ezvinhu": [
                {"prompt": "Bata mufananidzo wembwa. (Touch the dog.)", "choices": [("🐶", "imbwa"), ("🐱", "katsi"), ("🐄", "mombe")], "answer": "imbwa", "objective": "Identify familiar objects and animals in Shona."},
            ],
            "Machemero emhuka": [
                {"prompt": "Ndeipi mhuka inoti 'moo'? (Which animal says moo?)", "choices": [("🐄", "mombe"), ("🐔", "huku"), ("🐑", "gwai")], "answer": "mombe", "objective": "Match familiar animals to their sounds."},
            ],
            "Kwaziso ine rukudzo": [
                {"prompt": "Mangwanani! Ndeupi mufananidzo unoratidza kukwazisana?", "choices": [("👋", "kukwazisana"), ("😴", "kurara"), ("🍽️", "kudya")], "answer": "kukwazisana", "objective": "Recognise a respectful greeting."},
            ],
            "Kuverenga mifananidzo": [
                {"prompt": "Tarisa mufananidzo. Chii chiri mudenga?", "choices": [("☀️", "zuva"), ("🐟", "hove"), ("👟", "shangu")], "answer": "zuva", "objective": "Talk about familiar pictures in Shona."},
            ],
            "Nziyo nenhetembo": [
                {"prompt": "Ndeupi mufananidzo unoratidza kuimba?", "choices": [("🎤", "kuimba"), ("🛏️", "kurara"), ("🚗", "kutyaira")], "answer": "kuimba", "objective": "Recognise singing and participate in rhymes."},
            ],
        },
    },
    "English": {
        "icon": "🔤",
        "topics": {
            "Picture reading and storytelling": [
                {"prompt": "Look at the picture. What is the child doing?", "choices": [("🏃", "running"), ("😴", "sleeping"), ("🍽️", "eating")], "answer": "running", "objective": "Interpret a picture and use simple words."},
                {"prompt": "Which picture shows a rainy day?", "choices": [("☀️", "sunny"), ("🌧️", "rainy"), ("🌙", "night")], "answer": "rainy", "objective": "Answer a simple question about a picture."},
            ],
            "Vocabulary development": [
                {"prompt": "Touch the picture of a cat.", "choices": [("🐶", "dog"), ("🐱", "cat"), ("🐟", "fish")], "answer": "cat", "objective": "Recognise familiar English words through pictures."},
            ],
            "Listening and speaking": [
                {"prompt": "Which picture shows someone listening?", "choices": [("👂", "listening"), ("🏃", "running"), ("😴", "sleeping")], "answer": "listening", "objective": "Connect familiar actions with words."},
            ],
            "Alphabet recognition": [
                {"prompt": "Find the letter A.", "choices": [("B", "letter B"), ("A", "letter A"), ("C", "letter C")], "answer": "letter A", "objective": "Begin to recognise selected letters."},
            ],
            "Phonics and letter sounds": [
                {"prompt": "Which picture begins with the /b/ sound?", "choices": [("🍌", "banana"), ("🐟", "fish"), ("☀️", "sun")], "answer": "banana", "objective": "Match an initial sound to a familiar word."},
            ],
        },
    },
    "Social Science": {
        "icon": "🌍",
        "topics": {
            "My family": [
                {"prompt": "Which picture shows a family?", "choices": [("👨‍👩‍👧", "family"), ("🚗", "car"), ("🌳", "tree")], "answer": "family", "objective": "Recognise family and belonging."},
            ],
            "My school and community": [
                {"prompt": "Where do children go to learn?", "choices": [("🏫", "school"), ("🏥", "clinic"), ("🛒", "shop")], "answer": "school", "objective": "Identify familiar community places."},
            ],
            "Transport and road safety": [
                {"prompt": "Which picture shows a bus?", "choices": [("🚌", "bus"), ("🚲", "bicycle"), ("🚂", "train")], "answer": "bus", "objective": "Identify familiar forms of transport."},
            ],
            "Weather and seasons": [
                {"prompt": "Which picture shows rain?", "choices": [("☀️", "sun"), ("🌧️", "rain"), ("🌈", "rainbow")], "answer": "rain", "objective": "Recognise common weather conditions."},
            ],
            "Culture and heritage": [
                {"prompt": "Which picture shows people dancing together?", "choices": [("💃", "dancing"), ("🛌", "sleeping"), ("📚", "reading")], "answer": "dancing", "objective": "Recognise familiar cultural and social activities."},
            ],
        },
    },
    "Science and Technology": {
        "icon": "🔬",
        "topics": {
            "Living and non-living things": [
                {"prompt": "Touch something that is living.", "choices": [("🌳", "tree"), ("🪨", "stone"), ("🚗", "car")], "answer": "tree", "objective": "Begin to distinguish living and non-living things."},
            ],
            "Plants and their growth": [
                {"prompt": "What does a plant need to grow?", "choices": [("💧", "water"), ("🍬", "sweets"), ("📺", "television")], "answer": "water", "objective": "Recognise a basic need of plants."},
            ],
            "Animals and their habitats": [
                {"prompt": "Where does a fish live?", "choices": [("🌊", "water"), ("🌳", "tree"), ("🛏️", "bed")], "answer": "water", "objective": "Match animals to familiar habitats."},
            ],
            "The human body and senses": [
                {"prompt": "Which body part helps you hear?", "choices": [("👂", "ears"), ("👀", "eyes"), ("👃", "nose")], "answer": "ears", "objective": "Identify body parts and their functions."},
            ],
            "Materials and everyday technology": [
                {"prompt": "Which object helps us call someone?", "choices": [("📱", "phone"), ("🥄", "spoon"), ("🧦", "sock")], "answer": "phone", "objective": "Identify familiar tools and technology."},
            ],
        },
    },
    "Physical Education and Arts": {
        "icon": "🎨",
        "topics": {
            "Movement and balance": [
                {"prompt": "Which picture shows jumping?", "choices": [("🤸", "jumping"), ("😴", "sleeping"), ("📖", "reading")], "answer": "jumping", "objective": "Recognise and practise safe movements."},
            ],
            "Ball skills and games": [
                {"prompt": "Which object can you kick or throw in a game?", "choices": [("⚽", "ball"), ("📘", "book"), ("🥣", "bowl")], "answer": "ball", "objective": "Recognise equipment used in simple games."},
            ],
            "Drawing and colouring": [
                {"prompt": "Which tool can you use to colour a picture?", "choices": [("🖍️", "crayon"), ("🥄", "spoon"), ("🧦", "sock")], "answer": "crayon", "objective": "Identify tools for drawing and colouring."},
            ],
            "Painting and printing": [
                {"prompt": "Which tool can paint a picture?", "choices": [("🖌️", "paintbrush"), ("👟", "shoe"), ("🍎", "apple")], "answer": "paintbrush", "objective": "Explore art materials."},
            ],
            "Music, singing and dance": [
                {"prompt": "Which picture shows a musical instrument?", "choices": [("🥁", "drum"), ("🪑", "chair"), ("🍌", "banana")], "answer": "drum", "objective": "Recognise music and rhythm activities."},
            ],
            "Modelling and construction": [
                {"prompt": "Which material can you shape to make a model?", "choices": [("🟤", "play dough"), ("📱", "phone"), ("🥛", "cup")], "answer": "play dough", "objective": "Explore creating simple models."},
            ],
        },
    },
}

AVATARS = ["🦁", "🐘", "🦋", "🐼", "🐸", "🦒", "🐰", "🐢"]

if "learners" not in st.session_state:
    st.session_state.learners = []
if "results" not in st.session_state:
    st.session_state.results = []
if "active_learner" not in st.session_state:
    st.session_state.active_learner = None
if "activity" not in st.session_state:
    st.session_state.activity = None
if "teacher_unlocked" not in st.session_state:
    st.session_state.teacher_unlocked = False

def learner_by_id(learner_id):
    for learner in st.session_state.learners:
        if learner["id"] == learner_id:
            return learner
    return None

def get_questions(area, topic, age):
    items = AREAS[area]["topics"][topic]
    # Keep activities short and visual for children under six.
    if age < 6:
        return items[:1]
    return items

st.title("🌈 ECD Learn & Grow")
st.write("Picture-based learning for young children, with a separate teacher assessment area.")
st.caption("Prototype note: learner profiles and results currently remain in this browser session. They are not yet stored in a permanent shared database.")

home, learner_tab, teacher_tab = st.tabs(["🏠 Home", "🧒 Learner Mode", "👩‍🏫 Teacher Mode"])

with home:
    st.subheader("Welcome!")
    c1, c2 = st.columns(2)
    with c1:
        st.info("🧒 **Learner Mode**\n\nTap your picture, then choose a learning area and play.")
    with c2:
        st.info("👩‍🏫 **Teacher Mode**\n\nCreate profiles once, review results and record observations.")
    if not st.session_state.learners:
        st.warning("No learner profiles yet. The teacher should create learner profiles in Teacher Mode first.")
    else:
        st.success(f"{len(st.session_state.learners)} learner profile(s) available in this session.")

with learner_tab:
    st.subheader("Tap your picture to begin")
    if not st.session_state.learners:
        st.info("Ask your teacher to create your profile first.")
    else:
        cols = st.columns(2)
        for index, learner in enumerate(st.session_state.learners):
            with cols[index % 2]:
                if st.button(f"{learner['avatar']}  {learner['name']}", key=f"select_{learner['id']}", use_container_width=True):
                    st.session_state.active_learner = learner["id"]
                    st.session_state.activity = None
                    st.rerun()

    learner = learner_by_id(st.session_state.active_learner) if st.session_state.active_learner else None
    if learner:
        st.divider()
        st.markdown(f"## Hello, {learner['avatar']} {learner['name']}!")
        st.caption(f"Age: {learner['age']} | Learning level: {learner['level']}")
        area_names = list(AREAS.keys())
        selected_area = st.selectbox(
            "Choose a learning area",
            area_names,
            format_func=lambda name: f"{AREAS[name]['icon']}  {name}",
            key=f"area_{learner['id']}",
        )
        topic_names = list(AREAS[selected_area]["topics"].keys())
        selected_topic = st.selectbox("Choose a picture activity", topic_names, key=f"topic_{learner['id']}_{selected_area}")
        if st.button("🎲 Start activity", type="primary", use_container_width=True, key=f"start_{learner['id']}"):
            questions = get_questions(selected_area, selected_topic, learner["age"])
            st.session_state.activity = {
                "learner_id": learner["id"],
                "area": selected_area,
                "topic": selected_topic,
                "question_index": 0,
                "questions": questions,
                "correct": 0,
                "attempts": 0,
                "started": datetime.now().isoformat(timespec="seconds"),
            }
            st.rerun()

        activity = st.session_state.activity
        if activity and activity["learner_id"] == learner["id"]:
            q = activity["questions"][activity["question_index"]]
            st.divider()
            st.markdown(f"### {activity['area']}: {activity['topic']}")
            st.markdown(f"#### {q['prompt']}")
            st.caption(f"Learning goal: {q['objective']}")
            choice_cols = st.columns(len(q["choices"]))
            for i, (picture, label) in enumerate(q["choices"]):
                with choice_cols[i]:
                    st.markdown(f"<div style='font-size:42px;text-align:center;padding:8px'>{picture}</div>", unsafe_allow_html=True)
                    if st.button(label, key=f"answer_{learner['id']}_{activity['question_index']}_{i}", use_container_width=True):
                        activity["attempts"] += 1
                        is_correct = label == q["answer"]
                        if is_correct:
                            activity["correct"] += 1
                        st.session_state.results.append({
                            "learner_id": learner["id"],
                            "learner_name": learner["name"],
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "area": activity["area"],
                            "topic": activity["topic"],
                            "objective": q["objective"],
                            "answer": label,
                            "correct": is_correct,
                            "kind": "picture activity",
                        })
                        activity["last_answer"] = is_correct
                        activity["answered"] = True
                        st.rerun()
            if activity.get("answered"):
                if activity.get("last_answer"):
                    st.success("🌟 Well done! You got it right.")
                else:
                    st.info(f"Good try! The correct picture is: {q['answer']}. Let's keep learning.")
                if activity["question_index"] + 1 < len(activity["questions"]):
                    if st.button("Next picture ➜", type="primary", use_container_width=True):
                        activity["question_index"] += 1
                        activity.pop("answered", None)
                        activity.pop("last_answer", None)
                        st.rerun()
                else:
                    if st.button("Finish activity ⭐", type="primary", use_container_width=True):
                        st.session_state.results.append({
                            "learner_id": learner["id"],
                            "learner_name": learner["name"],
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "area": activity["area"],
                            "topic": activity["topic"],
                            "objective": "Activity completed",
                            "answer": f"{activity['correct']} correct out of {activity['attempts']} attempts",
                            "correct": activity["correct"] == activity["attempts"],
                            "kind": "activity summary",
                        })
                        st.session_state.activity = None
                        st.success("You finished! Ask your teacher to review your learning.")
                        st.rerun()
        if st.button("⬅️ Back to learner pictures", key=f"back_{learner['id']}"):
            st.session_state.active_learner = None
            st.session_state.activity = None
            st.rerun()

with teacher_tab:
    st.subheader("Teacher area")
    st.write("Create learner profiles once, then review their activity and add observations.")
    pin = st.text_input("Teacher PIN", type="password", help="Prototype PIN is 2468. Change this before using with real learners.")
    if st.button("Unlock Teacher Mode", use_container_width=True):
        if pin == os.environ.get("ECD_TEACHER_PIN", "2468"):
            st.session_state.teacher_unlocked = True
            st.success("Teacher Mode unlocked.")
        else:
            st.session_state.teacher_unlocked = False
            st.error("That PIN is not correct.")

    if st.session_state.teacher_unlocked:
        with st.expander("➕ Create a learner profile", expanded=not bool(st.session_state.learners)):
            with st.form("create_learner_form", clear_on_submit=True):
                name = st.text_input("Learner first name or nickname")
                age = st.selectbox("Age", [3, 4, 5, 6, 7, 8])
                level = st.selectbox("Current learning level", ["Needs support", "Developing", "Ready for a challenge"])
                interests = st.multiselect("Interests (optional)", ["Animals", "Songs", "Stories", "Drawing", "Movement", "Vehicles", "Plants"])
                support = st.selectbox("Activity support", ["Picture prompts", "Repeat instructions", "Extra practice", "No additional support"])
                avatar = st.selectbox("Choose a profile picture", AVATARS)
                submitted = st.form_submit_button("Save learner profile", use_container_width=True)
                if submitted:
                    if not name.strip():
                        st.error("Please enter a first name or nickname.")
                    elif any(x["name"].casefold() == name.strip().casefold() for x in st.session_state.learners):
                        st.error("A learner with that name is already listed. Use a unique nickname.")
                    else:
                        st.session_state.learners.append({
                            "id": f"learner_{len(st.session_state.learners)+1}_{int(datetime.now().timestamp())}",
                            "name": name.strip(),
                            "age": age,
                            "level": level,
                            "interests": interests,
                            "support": support,
                            "avatar": avatar,
                            "created": datetime.now().strftime("%Y-%m-%d"),
                        })
                        st.success(f"Profile created for {name.strip()}.")
                        st.rerun()

        if st.session_state.learners:
            st.markdown("### Learner profiles")
            for learner in st.session_state.learners:
                with st.expander(f"{learner['avatar']} {learner['name']} — age {learner['age']}"):
                    st.write(f"**Level:** {learner['level']}")
                    st.write(f"**Interests:** {', '.join(learner['interests']) or 'Not specified'}")
                    st.write(f"**Support:** {learner['support']}")
                    if st.button(f"Delete profile: {learner['name']}", key=f"delete_{learner['id']}"):
                        st.session_state.learners = [x for x in st.session_state.learners if x["id"] != learner["id"]]
                        st.session_state.results = [x for x in st.session_state.results if x["learner_id"] != learner["id"]]
                        if st.session_state.active_learner == learner["id"]:
                            st.session_state.active_learner = None
                        st.rerun()

            st.markdown("### Assessment and progress")
            learner_names = ["All learners"] + [x["name"] for x in st.session_state.learners]
            selected_learner_name = st.selectbox("Choose learner to review", learner_names)
            filtered = st.session_state.results
            if selected_learner_name != "All learners":
                filtered = [r for r in filtered if r["learner_name"] == selected_learner_name]

            if filtered:
                total = len([r for r in filtered if r["kind"] == "picture activity"])
                correct = len([r for r in filtered if r["kind"] == "picture activity" and r["correct"]])
                m1, m2, m3 = st.columns(3)
                m1.metric("Recorded answers", total)
                m2.metric("Correct", correct)
                m3.metric("Accuracy", f"{round(correct / total * 100) if total else 0}%")
                st.dataframe(
                    [{"Date": r["date"], "Learner": r["learner_name"], "Area": r["area"], "Topic": r["topic"], "Result": "Correct" if r["correct"] else "Practise again", "Type": r["kind"]} for r in filtered],
                    use_container_width=True,
                    hide_index=True,
                )
            else:
                st.info("No digital activity results recorded yet. Let a learner complete an activity first.")

            st.markdown("### Record a practical observation")
            with st.form("observation_form", clear_on_submit=True):
                obs_learner = st.selectbox("Learner", [x["name"] for x in st.session_state.learners], key="obs_learner")
                obs_area = st.selectbox("Learning area", list(AREAS.keys()), key="obs_area")
                obs_skill = st.text_input("Skill observed", placeholder="e.g. describes a picture in Shona")
                obs_rating = st.selectbox("Assessment", ["Achieved independently", "Achieved with support", "Needs more practice"])
                obs_note = st.text_area("Brief note (optional)", placeholder="What did you observe?")
                save_obs = st.form_submit_button("Save observation", use_container_width=True)
                if save_obs:
                    st.session_state.results.append({
                        "learner_id": next(x["id"] for x in st.session_state.learners if x["name"] == obs_learner),
                        "learner_name": obs_learner,
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "area": obs_area,
                        "topic": obs_skill or "Teacher observation",
                        "objective": obs_skill,
                        "answer": f"{obs_rating}. {obs_note}".strip(),
                        "correct": obs_rating == "Achieved independently",
                        "kind": "teacher observation",
                    })
                    st.success("Observation saved.")
                    st.rerun()

            export_rows = [
                {"date": r["date"], "learner": r["learner_name"], "area": r["area"], "topic_or_skill": r["topic"], "result": r["answer"], "record_type": r["kind"]}
                for r in st.session_state.results
            ]
            if export_rows:
                st.download_button(
                    "⬇️ Download assessment records (CSV)",
                    data=__import__("pandas").DataFrame(export_rows).to_csv(index=False).encode("utf-8"),
                    file_name="ecd_assessment_records.csv",
                    mime="text/csv",
                    use_container_width=True,
                )

st.divider()
st.caption("ECD Learn & Grow | A teaching prototype. A teacher should supervise learners and review practical skills.")
