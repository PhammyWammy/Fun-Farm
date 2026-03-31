import streamlit as st

plots1 = {
    "plant": "empty",
    "water": "not watered",
    "weeds": "no weeds"
    # ripe status goes here
}

plots2 = {
    "plant": "empty",
    "water": "not watered",
    "weeds": "weeds"
}

plots3 = {
    "plant": "empty",
    "water": "not watered",
    "weeds": "weeds"
}

plots4 = {
    "plant": "empty",
    "water": "not watered",
    "weeds": "weeds"
}

tomatoes = {
    "time to ripen": 3,
    "number of seeds": 2,
    "yield": 4,
    "ripe color": "bright red"
}

potatoes = {
    "time to ripen": 2,
    "number of seeds": 1,
    "yield": 3,
    "ripe color": "golden brown"
}

crops = {
    "tomatoes": tomatoes,
    "potatoes": potatoes
}

# seed PRICES (not amounts)
seeds = {
    "potato seed": 0.50,
    "tomato seed": 0.60
}

produce = {
    "potato": 1.50,
    "tomato": 2.25
}

user = {
    "money": 50,
    "user_seeds": {key: 0 for key, value in seeds.items()},
    "user_crops": {key: 0 for key, value in crops.items()},
    "water": 100,
    "plots owned": 1,
    "plots1": plots1,
    "plots2": plots2,
    "plots3": plots3,
    "plots4": plots4
}

st.set_page_config(page_title="Streamlit: Fun Farm", page_icon=":tractor:")

if "user" not in st.session_state:
    st.session_state["user"] = user

if "count" not in st.session_state:
    st.session_state["count"] = 0

st.title("Fun Farm")
money_col = st.columns([9, 1])

market_tab, field_tab = money_col[0].tabs(["Market", "Field"])

market_columns = market_tab.columns([5, 9])
market_columns[1].write("Welcome to the Market")

with market_tab.container(border=True):
    potatoseed_columns = st.columns(3)
    potatoseed_columns[0].text(f"Potato Seeds\n${seeds['potato seed']:.2f} per")
    if potatoseed_columns[2].button("Buy", key=1):
        if st.session_state["user"]["money"] < seeds["potato seed"]:
            st.toast("❌ You can't afford that!")
        else:
            st.session_state["user"]["user_seeds"]["potato seed"] += 1
            st.session_state["user"]["money"] -= seeds["potato seed"]
    potatoseed_columns[1].write(f"🥔seeds: {st.session_state['user']['user_seeds']['potato seed']}")

    tomatoseed_columns = st.columns(3)
    tomatoseed_columns[0].text(f"Tomato Seeds\n${seeds['tomato seed']:.2f} per")
    if tomatoseed_columns[2].button("Buy", key=2):
        if st.session_state["user"]["money"] < seeds["tomato seed"]:
            st.toast("❌ You can't afford that!")
        else:
            st.session_state["user"]["user_seeds"]["tomato seed"] += 1
            st.session_state["user"]["money"] -= seeds["tomato seed"]
    tomatoseed_columns[1].write(f"🍅seeds: {st.session_state['user']['user_seeds']['tomato seed']}")

with market_tab.container(border=True):
    potato_columns = st.columns(3)
    potato_columns[0].text(f"Potato\n${produce['potato']:.2f} per")
    if potato_columns[2].button("Sell", key=3):
        if st.session_state["user"]["user_crops"]["potatoes"] < 1:
            st.toast("❌ Not enough potatoes left!")
        else:
            st.session_state["user"]["user_crops"]["potatoes"] -= 1
            st.session_state["user"]["money"] += produce["potato"]
    potato_columns[1].write(f"🥔: {st.session_state['user']['user_crops']['potatoes']}")

    tomato_columns = st.columns(3)
    tomato_columns[0].text(f"Tomato\n${produce['tomato']:.2f} per")
    if tomato_columns[2].button("Sell", key=4):
        if st.session_state["user"]["user_crops"]["tomatoes"] < 1:
            st.toast("❌ Not enough potatoes left!")
        else:
            st.session_state["user"]["user_crops"]["tomatoes"] -= 1
            st.session_state["user"]["money"] += produce["tomato"]
    tomato_columns[1].write(f"🍅: {st.session_state['user']['user_crops']['tomatoes']}")

with market_tab.container(border=True):
    first_plot_columns = st.columns(2)
    with first_plot_columns[0].container(border=True):
        if st.session_state["user"]["plots owned"] >= 1:
            st.write("Purchased")
        st.write("Plot 1")

    with first_plot_columns[1].container(border=True):
        if st.session_state["user"]["plots owned"] >= 2:
            st.write("Purchased")
        else:
            st.write("Available")
            if st.button("$150"):
                if st.session_state["user"]["money"] < 150:
                    st.toast("❌ You can't afford that!")
                else:
                    st.session_state["user"]["plots owned"] += 1
                    st.session_state["user"]["money"] -= 150
        st.write("Plot 2")

    second_plot_columns = st.columns(2)
    with second_plot_columns[0].container(border=True):
        if st.session_state["user"]["plots owned"] >= 3:
            st.write("Purchased")
        else:
            st.write("Available")
            if st.button("$225"):
                if st.session_state["user"]["money"] < 225:
                    st.toast("❌ You can't afford that!")
                else:
                    st.session_state["user"]["plots owned"] += 1
                    st.session_state["user"]["money"] -= 225
        st.write("Plot 3")

    with second_plot_columns[1].container(border=True):
        if st.session_state["user"]["plots owned"] >= 4:
            st.write("Purchased")
        else:
            st.write("Available")
            if st.button("$300"):
                if st.session_state["user"]["money"] < 300:
                    st.toast("❌ You can't afford that!")
                else:
                    st.session_state["user"]["plots owned"] += 1
                    st.session_state["user"]["money"] -= 300
        st.write("Plot 4")

    if st.button("Purchase Water Refill for $25"):
        if st.session_state["user"]["money"] < 25:
            st.toast("❌ You can't afford that!")
        else:
            st.session_state["user"]["water"] = 100
            st.session_state["user"]["money"] -= 25

with field_tab:
    st.columns([5, 9])[1].write("Welcome to the Fields")
    plant_tab, water_tab, harvest_tab = st.tabs(["Plant", "Water", "Harvest"])

    with water_tab:
        water_columns = st.columns([1, 2, 2])
        with water_columns[0]:
            water_placeholder = st.empty()
            row_line = ""
            if st.button("Use water"):
                if st.session_state["user"]["water"] < 4:
                    st.toast("❌ You don't have enough water!")
                else:
                    st.session_state["user"]["water"] -= 4
                    st.session_state["user"]["plots1"]["water"] = "watered"
                    st.session_state["user"]["plots2"]["water"] = "watered"
                    st.session_state["user"]["plots3"]["water"] = "watered"
                    st.session_state["user"]["plots4"]["water"] = "watered"

            for i in range(25):
                if i * 4 >= (100 - st.session_state["user"]["water"]):
                    row_line += "🟦"
                else:
                    row_line += "⬛"
                if (i + 1) % 5 == 0:
                    st.write(row_line)
                    row_line = ""

        with water_columns[1]:
            with st.container(border=True):
                if st.session_state["user"]["plots owned"] > 0:
                    st.text(f"Plot 1\nStatus: {st.session_state['user']['plots1']['water']}")
                if st.session_state["user"]["plots owned"] > 1:
                    st.text(f"Plot 2\nStatus: {st.session_state['user']['plots2']['water']}")

        with water_columns[2]:
            with st.container(border=True):
                if st.session_state["user"]["plots owned"] > 2:
                    st.text(f"Plot 3\nStatus: {st.session_state['user']['plots3']['water']}")
                if st.session_state["user"]["plots owned"] > 3:
                    st.text(f"Plot 4\nStatus: {st.session_state['user']['plots4']['water']}")

    with harvest_tab:
        first_harvest_plots = st.columns(2)
        with first_harvest_plots[0].container(border=True):
            if st.session_state["user"]["plots owned"] >= 0:
                st.text(
                    f"Plot 1\nStatus: {st.session_state['user']['plots1']['water']}\n"
                    f"{st.session_state['user']['plots1']['weeds']}\n"
                    f"Crops: {st.session_state['user']['plots1']['plant']}"
                )
            with st.popover("Harvest"):
                if (
                    (st.session_state["user"]["plots1"]["weeds"] == "no weeds")
                    and (st.session_state["user"]["plots1"]["plant"] != "empty")
                    and (st.session_state["user"]["plots1"]["water"] == "watered")
                ):
                    if st.button("Harvest", key="harvest_plot1"):
                        plot1_crop = st.session_state["user"]["plots1"]["plant"]
                        st.session_state["user"]["user_crops"][plot1_crop] += crops[plot1_crop]["yield"]
                        st.session_state["user"]["plots1"]["plant"] = "empty"
                        st.session_state["user"]["plots1"]["weeds"] = "weeds"
                        st.session_state["user"]["plots1"]["water"] = "Not watered"

        with first_harvest_plots[1].container(border=True):
            if st.session_state["user"]["plots owned"] > 1:
                st.text(
                    f"Plot 2\nStatus: {st.session_state['user']['plots2']['water']}\n"
                    f"{st.session_state['user']['plots2']['weeds']}\n"
                    f"Crops: {st.session_state['user']['plots2']['plant']}"
                )
                with st.popover("Harvest"):
                    if (
                        (st.session_state["user"]["plots2"]["weeds"] == "no weeds")
                        and (st.session_state["user"]["plots2"]["plant"] != "empty")
                        and (st.session_state["user"]["plots2"]["water"] == "watered")
                    ):
                        if st.button("Harvest", key="harvest_plot2"):
                            plot2_crop = st.session_state["user"]["plots2"]["plant"]
                            st.session_state["user"]["user_crops"][plot2_crop] += crops[plot2_crop]["yield"]
                            st.session_state["user"]["plots2"]["plant"] = "empty"
                            st.session_state["user"]["plots2"]["weeds"] = "weeds"
                            st.session_state["user"]["plots2"]["water"] = "Not watered"

        second_harvest_plots = st.columns(2)
        with second_harvest_plots[0].container(border=True):
            if st.session_state["user"]["plots owned"] > 2:
                st.text(
                    f"Plot 3\nStatus: {st.session_state['user']['plots3']['water']}\n"
                    f"{st.session_state['user']['plots3']['weeds']}\n"
                    f"Crops: {st.session_state['user']['plots3']['plant']}"
                )
                with st.popover("Harvest"):
                    if (
                        (st.session_state["user"]["plots3"]["weeds"] == "no weeds")
                        and (st.session_state["user"]["plots3"]["plant"] != "empty")
                        and (st.session_state["user"]["plots3"]["water"] == "watered")
                    ):
                        if st.button("Harvest", key="harvest_plot3"):
                            plot3_crop = st.session_state["user"]["plots3"]["plant"]
                            st.session_state["user"]["user_crops"][plot3_crop] += crops[plot3_crop]["yield"]
                            st.session_state["user"]["plots3"]["plant"] = "empty"
                            st.session_state["user"]["plots3"]["weeds"] = "weeds"
                            st.session_state["user"]["plots3"]["water"] = "Not watered"

        with second_harvest_plots[1].container(border=True):
            if st.session_state["user"]["plots owned"] > 3:
                st.text(
                    f"Plot 4\nStatus: {st.session_state['user']['plots4']['water']}\n"
                    f"{st.session_state['user']['plots4']['weeds']}\n"
                    f"Crops: {st.session_state['user']['plots4']['plant']}"
                )
                with st.popover("Harvest"):
                    if (
                        (st.session_state["user"]["plots4"]["weeds"] == "no weeds")
                        and (st.session_state["user"]["plots4"]["plant"] != "empty")
                        and (st.session_state["user"]["plots4"]["water"] == "watered")
                    ):
                        if st.button("Harvest", key="harvest_plot4"):
                            plot4_crop = st.session_state["user"]["plots4"]["plant"]
                            st.session_state["user"]["user_crops"][plot4_crop] += crops[plot4_crop]["yield"]
                            st.session_state["user"]["plots4"]["plant"] = "empty"
                            st.session_state["user"]["plots4"]["weeds"] = "weeds"
                            st.session_state["user"]["plots4"]["water"] = "Not watered"

    with plant_tab.container(border=True):
        first_plant_plots = st.columns(2)

        with first_plant_plots[0].container(border=True):
            if st.session_state["user"]["plots owned"] >= 0:
                st.text(
                    f"Plot 1\nStatus: {st.session_state['user']['plots1']['water']}\n"
                    f"{st.session_state['user']['plots1']['weeds']}\n"
                    f"Crops: {st.session_state['user']['plots1']['plant']}"
                )
            with st.popover("Select"):
                if st.session_state["user"]["plots1"]["weeds"] == "weeds":
                    if st.button("Weed", key="weed_plot1"):
                        st.session_state["user"]["plots1"]["weeds"] = "no weeds"

                if st.session_state["user"]["plots1"]["plant"] == "empty":
                    # FIX: consume 1 seed (not price)
                    if st.button("Plant Tomatoes 🍅", key="pt_plot1"):
                        if st.session_state["user"]["user_seeds"]["tomato seed"] < 1:
                            st.toast("❌ You can't plant that!")
                        else:
                            st.session_state["user"]["user_seeds"]["tomato seed"] -= 1
                            st.session_state["user"]["plots1"]["plant"] = "tomatoes"

                    if st.button("Plant Potatoes 🥔", key="pp_plot1"):
                        if st.session_state["user"]["user_seeds"]["potato seed"] < 1:
                            st.toast("❌ You can't plant that!")
                        else:
                            st.session_state["user"]["user_seeds"]["potato seed"] -= 1
                            st.session_state["user"]["plots1"]["plant"] = "potatoes"

        with first_plant_plots[1].container(border=True):
            if st.session_state["user"]["plots owned"] > 1:
                st.text(
                    f"Plot 2\nStatus: {st.session_state['user']['plots2']['water']}\n"
                    f"{st.session_state['user']['plots2']['weeds']}\n"
                    f"Crops: {st.session_state['user']['plots2']['plant']}"
                )
                with st.popover("Select"):
                    if st.session_state["user"]["plots2"]["weeds"] == "weeds":
                        if st.button("Weed", key="weed_plot2"):
                            st.session_state["user"]["plots2"]["weeds"] = "no weeds"

                    if st.session_state["user"]["plots2"]["plant"] == "empty":
                        # FIX: consume 1 seed (not price)
                        if st.button("Plant Tomatoes 🍅", key="pt_plot2"):
                            if st.session_state["user"]["user_seeds"]["tomato seed"] < 1:
                                st.toast("❌ You can't plant that!")
                            else:
                                st.session_state["user"]["user_seeds"]["tomato seed"] -= 1
                                st.session_state["user"]["plots2"]["plant"] = "tomatoes"

                        if st.button("Plant Potatoes 🥔", key="pp_plot2"):
                            if st.session_state["user"]["user_seeds"]["potato seed"] < 1:
                                st.toast("❌ You can't plant that!")
                            else:
                                st.session_state["user"]["user_seeds"]["potato seed"] -= 1
                                st.session_state["user"]["plots2"]["plant"] = "potatoes"

        second_plant_plots = st.columns(2)

        with second_plant_plots[0].container(border=True):
            if st.session_state["user"]["plots owned"] > 2:
                st.text(
                    f"Plot 3\nStatus: {st.session_state['user']['plots3']['water']}\n"
                    f"{st.session_state['user']['plots3']['weeds']}\n"
                    f"Crops: {st.session_state['user']['plots3']['plant']}"
                )
                with st.popover("Select"):
                    if st.session_state["user"]["plots3"]["weeds"] == "weeds":
                        if st.button("Weed", key="weed_plot3"):
                            st.session_state["user"]["plots3"]["weeds"] = "no weeds"

                    if st.session_state["user"]["plots3"]["plant"] == "empty":
                        # FIX: consume 1 seed (not price)
                        if st.button("Plant Tomatoes 🍅", key="pt_plot3"):
                            if st.session_state["user"]["user_seeds"]["tomato seed"] < 1:
                                st.toast("❌ You can't plant that!")
                            else:
                                st.session_state["user"]["user_seeds"]["tomato seed"] -= 1
                                st.session_state["user"]["plots3"]["plant"] = "tomatoes"

                        if st.button("Plant Potatoes 🥔", key="pp_plot3"):
                            if st.session_state["user"]["user_seeds"]["potato seed"] < 1:
                                st.toast("❌ You can't plant that!")
                            else:
                                st.session_state["user"]["user_seeds"]["potato seed"] -= 1
                                st.session_state["user"]["plots3"]["plant"] = "potatoes"

        with second_plant_plots[1].container(border=True):
            if st.session_state["user"]["plots owned"] > 3:
                st.text(
                    f"Plot 4\nStatus: {st.session_state['user']['plots4']['water']}\n"
                    f"{st.session_state['user']['plots4']['weeds']}\n"
                    f"Crops: {st.session_state['user']['plots4']['plant']}"
                )
                with st.popover("Select"):
                    if st.session_state["user"]["plots4"]["weeds"] == "weeds":
                        if st.button("Weed", key="weed_plot4"):
                            st.session_state["user"]["plots4"]["weeds"] = "no weeds"

                    if st.session_state["user"]["plots4"]["plant"] == "empty":
                        # FIX: consume 1 seed (not price)
                        if st.button("Plant Tomatoes 🍅", key="pt_plot4"):
                            if st.session_state["user"]["user_seeds"]["tomato seed"] < 1:
                                st.toast("❌ You can't plant that!")
                            else:
                                st.session_state["user"]["user_seeds"]["tomato seed"] -= 1
                                st.session_state["user"]["plots4"]["plant"] = "tomatoes"

                        if st.button("Plant Potatoes 🥔", key="pp_plot4"):
                            if st.session_state["user"]["user_seeds"]["potato seed"] < 1:
                                st.toast("❌ You can't plant that!")
                            else:
                                st.session_state["user"]["user_seeds"]["potato seed"] -= 1
                                st.session_state["user"]["plots4"]["plant"] = "potatoes"

# Show the user their inventory
water_placeholder.write(f"Tank Status: {st.session_state['user']['water']}%")
money_col[1].write(f"${st.session_state['user']['money']:.2f}")

st.session_state["count"] += 1
if st.session_state["user"]["money"] > 2000:
    if st.session_state["user"]["plots owned"] >= 4:
        st.balloons()
        st.write(f"You win! With a count of {st.session_state['count']}.")

#st.write(st.session_state["user"])
#st.write(crops)

#type(5) integer or 'int'
#type("abce") string or 'str'
#type("5") is string!

#str(5) means "make it a string"
#int("5") means "make it an integer"
#st.write(st.session_state)
#Abraham laughed at a single program 😔

#String magic
#string1 = "I am a string"
#string2 = "My name is Jonathan"
#print(string1+string2)

#list1 = ["a", 4, 3, string1]
#print(list1[0])
#dict1 = {}

#list4 = ["a", 15,"I am Jonathan Pham", "April 2, 2010", "Who're you"]
