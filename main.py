
import random
import streamlit as st
from PyBypass.main import BypasserNotFoundError, UnableToBypassError, UrlConnectionError
import PyBypass as bypasser
from streamlit_extras.buy_me_a_coffee import button

st.set_page_config(page_title="URL Bypasser", page_icon='🧊',
                   layout="centered", initial_sidebar_state="auto",    menu_items={
                       'Get Help': 'https://telegram.me/ask_admin001',
                       'Report a bug': "https://telegram.me/ask_admin001",
                       'About': "This is URL Bypasser for ADLINKFLY based website. Made by [Kevin](https://github.com/kevinnadar22)"
                   })


def random_celeb():
    return random.choice([st.balloons(), st.snow()])

st.title("URL Bypasser")
tab1, tab2 = st.tabs(["Bypass", "Available Websites", ])

__avl_website__ = ['try2link.com', ' adf.ly', ' bit.ly', ' ouo.io', ' ouo.press', ' shareus.in', ' shortly.xyz', ' tinyurl.com', ' thinfi.com', ' hypershort.com ', 'safeurl.sirigan.my.id', ' gtlinks.me', ' loan.kinemaster.cc', ' theforyou.in', ' linkvertise.com', ' shorte.st', ' earn4link.in', ' tekcrypt.in', ' link.short2url.in', ' go.rocklinks.net', ' rocklinks.net', ' earn.moneykamalo.com', ' m.easysky.in', ' indianshortner.in', ' open.crazyblog.in', ' link.tnvalue.in',' shortingly.me', ' open2get.in', ' dulink.in', ' bindaaslinks.com', ' za.uy', ' pdiskshortener.com', ' mdiskshortner.link', ' go.earnl.xyz', ' g.rewayatcafe.com', ' ser2.crazyblog.in', ' bitshorten.com', ' rocklink.in', ' droplink.co', ' tnlink.in', ' ez4short.com', ' xpshort.com', ' vearnl.in', ' adrinolinks.in', ' techymozo.com', ' linkbnao.com', ' linksxyz.in', ' short-jambo.com', ' ads.droplink.co.in', ' linkpays.in', ' pi-l.ink', ' link.tnlink.in ', ' pkin.me']

with tab1:
    show_alert = False
    url = st.text_input(label="Paste your URL")
    if st.button("Submit"):
        if url:
            try:

                with st.spinner("Loading..."):
                    bypassed_link = bypasser.bypass(url)
                    st.success(bypassed_link)

                random_celeb()

                with st.expander("Copy"):
                    st.code(bypassed_link)

            except (UnableToBypassError, BypasserNotFoundError, UrlConnectionError) as e:
                if show_alert := True:
                    st.error(e)

            if st.button("Dismiss"):
                show_alert = False

        elif show_alert := True:
            st.error("No URLS found")

with tab2:
    st.subheader("Available Websites")
    st.table(__avl_website__)

button(username="kevinadar22", floating=1, width=221)
