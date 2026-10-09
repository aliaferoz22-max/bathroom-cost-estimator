import streamlit as st

st.set_page_config(
    page_title="UK Bathroom Renovation Cost Estimator",
    page_icon="🛁",
    layout="centered",
)

st.title("🛁 UK Bathroom Renovation Cost Estimator")
st.write(
    "Planning a bathroom renovation? Answer a few questions to get a "
    "**rough cost range** for a typical UK bathroom project. These are "
    "ballpark figures to help you budget — always get quotes from local "
    "tradespeople before committing."
)

st.divider()

# --- Inputs ---
size = st.selectbox(
    "Bathroom size",
    ["Small (cloakroom / en-suite)", "Standard family bathroom", "Large bathroom"],
    index=1,
)

scope = st.radio(
    "Renovation scope",
    [
        "Refresh (new suite, taps & tiling kept simple)",
        "Mid-range (new suite, tiling, flooring & lighting)",
        "Full renovation (rip-out, re-tiling, new plumbing positions)",
    ],
    index=1,
)

quality = st.select_slider(
    "Fittings quality",
    options=["Budget", "Mid-range", "Premium"],
    value="Mid-range",
)

location = st.selectbox(
    "Where in the UK?",
    ["North / Midlands / Wales / NI", "South East", "London"],
    index=0,
)

if st.button("Estimate my cost", type="primary"):
    # Base ranges (labour + materials), GBP — deliberately hedged
    base = {
        "Small (cloakroom / en-suite)": (2500, 4500),
        "Standard family bathroom": (4000, 8000),
        "Large bathroom": (6500, 12000),
    }[size]

    scope_mult = {
        "Refresh (new suite, taps & tiling kept simple)": 0.7,
        "Mid-range (new suite, tiling, flooring & lighting)": 1.0,
        "Full renovation (rip-out, re-tiling, new plumbing positions)": 1.35,
    }[scope]

    quality_mult = {"Budget": 0.85, "Mid-range": 1.0, "Premium": 1.4}[quality]

    location_mult = {
        "North / Midlands / Wales / NI": 0.9,
        "South East": 1.1,
        "London": 1.25,
    }[location]

    low = int(base[0] * scope_mult * quality_mult * location_mult / 100) * 100
    high = int(base[1] * scope_mult * quality_mult * location_mult / 100) * 100

    st.divider()
    st.subheader("Your estimated range")
    st.markdown(f"## £{low:,} – £{high:,}")
    st.caption(
        "Rough estimate including typical labour and materials. "
        "Complex plumbing moves, structural work or high-end stone can push costs higher."
    )

    st.info(
        "💡 **Tip:** Set aside a 10–15% contingency on top of your budget "
        "for surprises behind the tiles."
    )

st.divider()
st.markdown(
    "### Want the full planning guide?\n"
    "Read our detailed UK bathroom renovation guide with cost breakdowns, "
    "timelines and planning checklists:"
)
st.link_button(
    "📖 Bathroom Renovation Guide",
    "https://home-refurbishment.co.uk/bathroom-renovation/",
)

st.caption(
    "Built by Home Refurbishment UK — practical home improvement guides for UK homes. "
    "Estimates are indicative only, not quotes."
)
