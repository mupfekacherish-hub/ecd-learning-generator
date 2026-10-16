import streamlit as st
from supabase import create_client

st.set_page_config(
    page_title="ECD Learn & Grow",
    page_icon="🌱",
    layout="wide"
)


@st.cache_resource
def connect_database():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


try:
    supabase = connect_database()
    database_ready = True
except Exception:
    supabase = None
    database_ready = False


TOPICS = {
    "Mathematics": [
        "Counting", "Number recognition", "Shapes",
        "Sizes and patterns", "Sorting and matching"
    ],
    "English": [
        "Phonics", "Letter recognition", "Vocabulary",
        "Picture reading", "Storytelling"
    ],
    "Shona": [
        "Kwazisana", "Mhuka dzepamba", "Machemero emhuka",
        "Nhetembo", "Kutaura nyaya"
    ],
    "Science and Technology": [
        "Weather", "Plants", "Domestic animals",
        "Simple experiments", "Everyday tools"
    ],
    "Social Science": [
        "Family", "Community helpers", "Culture and heritage",
        "Transport", "Child rights"
    ],
    "Physical Education and Arts": [
        "Kicking", "Jumping and balancing",
        "Drawing and colouring", "Singing and dancing",
        "Modelling"
    ]
}

INTERESTS = ["Songs", "Games", "Stories", "Drawing", "Movement"]
LEVELS = ["Needs support", "Developing", "Challenging"]
SUPPORTS = ["None", "Visual aids", "Repetition"]


def make_activity(area, topic, age, level, interest, support):
    young = age == "Under 6 years"

    objectives = {
        "Mathematics": f"Practise {topic.lower()} using objects and play.",
        "English": f"Develop language skills through {topic.lower()}.",
        "Shona": f"Practise Shona language through {topic.lower()}.",
        "Science and Technology": f"Explore {topic.lower()} through observation.",
        "Social Science": f"Understand {topic.lower()} through discussion and role-play.",
        "Physical Education and Arts": f"Develop physical or creative skills through {topic.lower()}."
    }

    materials = {
        "Mathematics": "Bottle tops, sticks, blocks or number cards.",
        "English": "Picture cards, letter cards, books or paper.",
        "Shona": "Pictures, familiar objects and Shona word cards.",
        "Science and Technology": "Safe everyday objects and pictures.",
        "Social Science": "Pictures and familiar role-play objects.",
        "Physical Education and Arts": "Paper, crayons, safe modelling materials or open space."
    }

    tasks = {
        "Mathematics": f"Use objects to practise {topic.lower()}.",
        "English": f"Practise {topic.lower()} using words, sounds or pictures.",
        "Shona": f"Practise {topic.lower()} using familiar Shona words.",
        "Science and Technology": f"Explore {topic.lower()} through safe observation.",
        "Social Science": f"Discuss or role-play a situation about {topic.lower()}.",
        "Physical Education and Arts": f"Practise {topic.lower()} through a safe creative or movement activity."
    }

    interest_ideas = {
        "Songs": "Include a simple song, rhythm or chant.",
        "Games": "Turn the task into a short learning game.",
        "Stories": "Introduce the task through a short story.",
        "Drawing": "Invite the learner to draw something related to the topic.",
        "Movement": "Include safe movements or gestures."
    }

    support_ideas = {
        "None": "Encourage the learner and check understanding.",
        "Visual aids": "Use clear pictures, objects and demonstrations.",
        "Repetition": "Repeat instructions and allow extra practice."
    }

    if level == "Needs support":
        teaching = "Demonstrate each step and guide the learner."
    elif level == "Developing":
        teaching = "Demonstrate once and give prompts when needed."
    else:
        teaching = "Encourage independent work and explanations."

    if young:
        steps = [
            "Show a picture or real object related to the topic.",
            f"Help the learner to {tasks[area].lower()}",
            "Let the learner practise through play.",
            "Praise the learner and ask a simple question."
        ]
        duration = "10–15 minutes"
    else:
        steps = [
            "Introduce the topic and discuss what the learner knows.",
            f"Demonstrate how to {tasks[area].lower()}",
            "Ask the learner to complete the task.",
            "Review the work and give feedback."
        ]
        duration = "20–30 minutes"

    assessment = {
        "Needs support": "Check whether the learner participates with guidance.",
        "Developing": "Check whether the learner completes the task with some prompts.",
        "Challenging": "Check whether the learner completes the task independently."
    }

    return {
        "objective": objectives[area],
        "materials": materials[area],
        "task": tasks[area],
        "steps": steps,
        "duration": duration,
        "teaching": teaching,
        "interest": interest_ideas[interest],
        "support": support_ideas[support],
        "assessment": assessment[level]
    }


def show_activity(area, topic, age, level, interest, support):
    activity = make_activity(
        area, topic, age, level, interest, support
    )

    st.success("Your learning activity is ready!")

    st.write("**Learning area:**", area)
    st.write("**Topic:**", topic)
    st.write("**Age group:**", age)
    st.write("**Duration:**", activity["duration"])

    st.subheader("Learning objective")
    st.write(activity["objective"])

    st.subheader("Materials")
    st.write(activity["materials"])

    st.subheader("Activity")
    st.write(activity["task"])
    st.write(activity["interest"])

    st.subheader("Teaching steps")
    for i, step in enumerate(activity["steps"], 1):
        st.write(f"{i}. {step}")

    st.subheader("Individual support")
    st.write(activity["teaching"])
    st.write(activity["support"])

    st.subheader("Assessment")
    st.write(activity["assessment"])


st.title("🌱 ECD Learn & Grow")
st.write("Individualised Learning Activity Generator")
st.caption(
    "Designed to help teachers prepare activities and support young learners."
)

mode = st.radio(
    "Choose a mode",
    ["Teacher Mode 👩‍🏫", "Learner Mode 🧒"],
    horizontal=True
)

if mode == "Teacher Mode 👩‍🏫":
    st.header("👩‍🏫 Teacher Mode")

    if not database_ready:
        st.error(
            "Database connection failed. Check SUPABASE_URL, "
            "SUPABASE_KEY and the Streamlit Cloud logs."
        )
    else:
        st.subheader("1. Register a learner")

        with st.form("register_learner"):
            learner_name = st.text_input("Learner name or ID")

            learner_age = st.selectbox(
                "Age group",
                ["Under 6 years", "7–8 years"]
            )

            learner_level = st.selectbox(
                "Ability level", LEVELS
            )

            learner_interest = st.selectbox(
                "Interests", INTERESTS
            )

            learner_support = st.selectbox(
                "Additional support", SUPPORTS
            )

            save_learner = st.form_submit_button(
                "Save Learner Permanently"
            )

        if save_learner:
            if not learner_name.strip():
                st.warning("Enter a learner name or ID.")
            else:
                try:
                    result = supabase.table("learners").insert({
                        "learner_name": learner_name.strip(),
                        "age_group": learner_age,
                        "ability_level": learner_level,
                        "interests": learner_interest,
                        "support_needs": learner_support
                    }).execute()

                    if result.data:
                        st.success("Learner saved successfully!")
                    else:
                        st.error("No learner record was returned.")
                except Exception:
                    st.error(
                        "Could not save the learner. Check that the "
                        "learners table exists and database permissions "
                        "allow this operation."
                    )

        st.divider()
        st.subheader("2. Registered learners")

        try:
            response = (
                supabase.table("learners")
                .select(
                    "id, learner_name, age_group, ability_level, "
                    "interests, support_needs"
                )
                .order("id", desc=True)
                .execute()
            )

            learners = response.data or []

            if learners:
                st.dataframe(
                    [
                        {
                            "ID": learner["id"],
                            "Learner": learner["learner_name"],
                            "Age": learner["age_group"],
                            "Ability": learner["ability_level"],
                            "Interest": learner["interests"],
                            "Support": learner["support_needs"]
                        }
                        for learner in learners
                    ],
                    use_container_width=True
                )

                learner_options = {
                    f'{item["learner_name"]} (ID: {item["id"]})': item
                    for item in learners
                }

                selected_label = st.selectbox(
                    "Select a learner for an activity",
                    list(learner_options.keys())
                )

                selected = learner_options[selected_label]

                st.divider()
                st.subheader("3. Generate an individualised activity")

                with st.form("teacher_activity"):
                    area = st.selectbox(
                        "Learning area", list(TOPICS.keys())
                    )
                    topic = st.selectbox(
                        "Topic", TOPICS[area]
                    )
                    generate = st.form_submit_button(
                        "Generate Teaching Plan"
                    )

                if generate:
                    show_activity(
                        area,
                        topic,
                        selected["age_group"],
                        selected["ability_level"],
                        selected["interests"],
                        selected["support_needs"]
                    )

            else:
                st.info(
                    "No learners registered yet. Register a learner above."
                )

        except Exception:
            st.error(
                "Could not load learner records. Check the table "
                "and database permissions."
            )


else:
    st.header("🧒 My Learning Corner")
    st.write("Hello! Choose a topic and let's learn. 🌈")

    age = st.selectbox(
        "Your age group",
        ["Under 6 years", "7–8 years"],
        key="child_age"
    )

    area = st.selectbox(
        "What would you like to learn?",
        list(TOPICS.keys()),
        key="child_area"
    )

    topic = st.selectbox(
        "Choose a topic",
        TOPICS[area],
        key="child_topic"
    )

    interest = st.selectbox(
        "Choose how you want to learn",
        INTERESTS,
        key="child_interest"
    )

    if st.button("Let's Learn! 🌟"):
        show_activity(
            area,
            topic,
            age,
            "Developing",
            interest,
            "Visual aids"
        )
        st.balloons()

st.divider()
st.caption(
    "Learner records are stored in Supabase when database access "
    "is configured. Child-facing mode does not display the learner register."
)
