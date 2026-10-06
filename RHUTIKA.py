import streamlit as st 
import pandas as pd 
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt 

st.set_page_config(
    page_title="RHUTIKA Eco-Shield | CEO Dashboard",
    page_icon="🚀",
    layout="wide"
)

#custom Avant-Garde Premium Branding CSS
st.markdown("""
<style>
.main-title {font-size: 42px; font-weight: bold; color: #6A1B9A; text-align: center; margin-bottom: 5px;}
.subtitle { font-size: 18px; text-align: center; color: #37474F; margin-bottom: 30px;}
.metric-box { padding: 15px; background-color: #F3E5F5; border-left: 5px solid #8E24AA; border-radius: 5px; color: #212121;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title"> RHUTIKA ECO-SHIELD AVANT-GARDE COUTURE</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Deep-Tech Core Materials R&D & Global Supply Chain Predictive Engine</div>', unsafe_allow_html=True)

#Sidebar Personal Navigation Panel
st.sidebar.header("👑CEO Control Room")
st.sidebar.markdown(f"**Founder:** Rhutika Kshirsagar")
st.sidebar.markdown(f"**Affiliation:** IIT Bhubaneswar")
st.sidebar.markdown("---")
app_mode = st.sidebar.radio("Navigate Enterprise Modules",[
    "1. Thin-Film Interference Tint Designer",
    "2. Quantum UV Band-Gap Automator",
    "3. Artisanal Logistics & Profit Margin Tracker"
])

#MODULE 1: THIN-FILM INTERFERENCE TINT DESIGNER (The Dye-Free Physics)

if app_mode == "1. Thin-Film Interference Tint Designer":
    st.header("🔬 Structural Wave Interference Tint Designer")
    st.markdown("🗑️ *Eliminating chemical textile dyes by mathematically calculating constructive wave interference thickness on protein substrates.*")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Design Specifications")
        target_color = st.selectbox("Select Target Runway Color", ["Gold","Emerald Green", "Royal Blue", "Avant-Garde Violet"])
        refractive_index_zno = st.slider("Zno Coating Refractive Index (n_f)", 1.90, 2.10, 2.00, step=0.01)
        interference_order = st.selectbox("Interference Order (m)", [0, 1, 2])

        #Physics Mapping: Map colors to exact center wavelengths (nm)
        color_wavelengths = {"Gold": 500, "Emerald Green": 530, "Royal Blue": 460, "Avant-Garde Violet": 410}
        lambda_target = color_wavelengths[target_color]

        #Core Math Execution: 2 * n_f * t = (m + 0.5) * Lamba
        #Therefore: t = ((m + 0.05) * Lambda) / ( 2 * n_f )
        required_thickness = ((interference_order + 0.5) * lambda_target) / (2 * refractive_index_zno)

    with col2:
        st.markdown(f"<div class= 'metric-box'> <h3> 🎯 Target Calculation Result </h3>"
                        f" To reflect <b> {target_color}</b> (\u03bb = {lambda_target} nm) at order m = {interference_order}, "
                        f"your automated sol-gel line must deposit a highly precise crystalline Zno nano-layer of "
                        f"<b>{required_thickness:.2f} nm</b> around the silk fiber core.</div>", unsafe_allow_html=True)
            
        # Visualising the wave interference threshold
        fig, ax = plt.subplots(figsize=(6, 2.5))
        x = np.linspace(350, 750, 500)
        #simulate a clean Gaussian reflectance peak centered at the target color
        y = np.exp(-((x - lambda_target) / 30)**2)
        ax.plot(x, y, color="#8E24AA", linewidth=2)
        ax.axvline(lambda_target, linestyle="--", color="black", label=f"Reflectance Max: {lambda_target}nm")
        ax.set_title("Predictive Multi-Spectral Reflectance Profile")
        ax.set_xlabel("Wavelength (nm)")
        ax.set_ylabel("Reflectance Intensity")
        ax.legend()
        st.pyplot(fig)

#MODULE 2: QUANTUM UV BAND-GAP AUTOMATOR (The Lab Verification Data Engine)

elif app_mode == "2. Quantum UV Band-Gap Automator":
    st.header("⚛️ Quantum Band-Gap Analytical Engine (Taauc Plot Automator)")
    st.markdown("📊 *Processing raw UV-Vis spectrometer logs to isolate the exact optical band gap (E_g) required for permanent solar UV protection.*")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Lab Simulation COntrols")
        st.markdown("Simulating raw instrumentation outputs matching your low-temperature (135°C) curing lines.")
        sample_purity = st.slider("Crystalline Annealing Quality Factor", 0.85, 1.00, 0.95, step=0.01)

        #Generating standard synthetic UV-Vis absorption database matching pure direct ZnO (Bandgap ~3.25 eV)
        energies = np.linspace(2.5, 4.0, 100) #Photon Energy in eV
        #Construct direct allowed absoorption coefficient baseline: alpha proportional to sqrt(h_nu - E_g)
        true_eg = 3.25 / sample_purity
        alpha = np.where(energies > true_eg, 50 * np.sqrt(np.maximum(0, energies - true_eg)), 1.5 * np.random.normal(0, 0.2, 100))
        alpha_hnu_squared = (alpha * energies) ** 2

        df = pd.DataFrame({"Photon_Energy_eV": energies, "Alpha_hnu_Squared":  alpha_hnu_squared})

        #Apply SciPy Linear Regression on the straight linear segment to calculate the intercept (E_g)
        linear_segment = df[(df["Photon_Energy_eV"] >= 3.4) & (df["Photon_Energy_eV"] <= 3.8)]
        slope, intercept, r_value, p_value, std_err = stats.linregress(linear_segment["Photon_Energy_eV"], linear_segment["Alpha_hnu_Squared"])
        calculated_eg = -intercept / slope #where y = 0

    with col2:
        st.markdown(f"<div class='metric-box'><h3>📈 Automated Spectroscopic Intercept</h3>"
                    f"<b>Extrapolated Optical Band Gap (E_g):</b> {calculated_eg:.3f} eV<br>"
                    f"<b>Statistical Code Consistency (R² Value):</b> {r_value**2:.4f}</div>", unsafe_allow_html=True)

        #Plotting the formal Tauc Plot Configuration
        fig, ax = plt.subplots(figsize=(7, 3.5))
        ax.scatter(df["Photon_Energy_eV"], df["Alpha_hnu_Squared"], color="#D32F2F", s=10, label="Raw Spactra Data")
        #Line fir visualisation
        x_fit = np.linspace(calculated_eg, 4.0, 50)
        y_fit = slope * x_fit + intercept
        ax.plot(x_fit, y_fit, color="black", linestyle="-", label="Tauc Linear Fit Extrapolation")
        ax.axvline(calculated_eg, color="blue", linestyle=":", label=f"E_g Intercept = {calculated_eg:.2f} eV")
        ax.set_ylim(0, max(alpha_hnu_squared) * 1.1)
        ax.set_xlabel("Photon Energy, h\u03bd (eV)")
        ax.set_ylabel("(\u03b1h\u03bd)\u00b2 (arbitrary units)")
        ax.set_title("Crystalline Direct Allowed Electronic Transition Profile")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)


# MODULE 3: ARTISANAL LOGISTICS & CAPITAL MARGIN TRACKER 
elif app_mode == "3. Artisanal Logistics & Profit Margin Tracker":
    st.header("👔 Corporate Operations Sourcing & Venture Unit Economics")
    st.markdown("💰*Proving business viability to venture capital funds by scaling premium markups while uplifting India artisan weaving clusters.*")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Sourcing Expenses & Premium Configuration")
        raw_yarn_cost_inr = st.number_input("Raw Handloom Yarn Cost per Meter (Paid to Weavers in INR)", 200, 1000, 500)
        sol_gel_coating_cost_inr = st.number_input("Cleanroom Curing & Material Processing Cost per Meter (INR)", 50, 500, 150)
        premium_tailoring_cost_inr = st.number_input("High-Fashion Avant-Garde Construction Cost per Garment (INR)", 2000, 20000, 5000)
        fabric_required = st.slider("Meters of Protective Fabric Required per Dress", 2.0, 10.0, 4.5, step=0.5)

        #calculate Total Cost of Production (COGS)
        total_fabric_cogs = (raw_yarn_cost_inr + sol_gel_coating_cost_inr) * fabric_required
        total_production_cogs = total_fabric_cogs + premium_tailoring_cost_inr

    with col2:
        st.subheader("Luxury Retail Projections")
        target_luxury_tier = st.select_slider("Target Retail Market Positioning", ["Premium Retail", "High-End Luxury Boutique", "Global Avant-Garde Runway Showcase"])

        # Pricing strategy dictionary matching true luxury industry multipliers
        pricing_multiplier = {"Premium Retail": 3.5, "High-End Luxury Boutique": 6.0, "Global Avant-Garde Runway Showcase": 12.0}
        multiplier = pricing_multiplier[target_luxury_tier]

        final_retail_price = total_production_cogs * multiplier
        net_profit_per_garment = final_retail_price - total_production_cogs
        profit_margin_percent = (net_profit_per_garment / final_retail_price) * 100

        st.markdown(f"<div class='metric-box' style='background-color: #E8F5E9; border-left: 5px solid #2E7D32;'>"
                    f"<h3>📊 Venture Financial Analytics Summary</h3>"
                    f"<b>Total Unit COGS: </b> \u20b9{total_production_cogs:,.2f}<br>"
                    f"<b>Runway Selling Retail Price:</b> \u20b9{final_retail_price:,.2f}<br>"
                    f"<b>Net Profit Margin per Piece: </b> \u20b9 {net_profit_per_garment:,.2f}<br>"
                    f"<b> Gross Capital Margin Efficiency: </b> {profit_margin_percent:,.1f}%</div>", unsafe_allow_html=True)

        #Visualising the unit allocation breakdown for your board meetings
        fig, ax = plt.subplots(figsize=(5, 5))
        costs = [total_fabric_cogs, premium_tailoring_cost_inr, net_profit_per_garment]
        labels = ['Fabric COGS', 'Tailoring COGS', 'Net Margin']
        ax.pie(costs, labels=labels, autopct='%1.1f%%', colors=['#8E24AA', '#BA68C8', '#2E7D32'], startangle=140)
        ax.set_title("Unit Price Allocation Breakdown")
        st.pyplot(fig)



        
            

        
        


