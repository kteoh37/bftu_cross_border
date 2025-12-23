# Cross-Border Flow Restrictions Data (BFTU Data)

This repository contains comprehensive datasets on cross-border flow restrictions from the paper:

**"Expanding the Landscape of Cross-Border Flow Restrictions: Modern Tools and Historical Perspectives"**
By Katharina Bergant (IMF & CEPR), Andrés Fernández (IMF), Ken Teoh (IMF), and Martín Uribe (Columbia University & NBER), 2025

The data can be used freely and without further permission as long as explicit reference is made to the above paper.

---

**Disclaimer:** *The data reflect the authors' interpretation and codification of information provided in the IMF's Annual Report on Exchange Rate Arrangements and Restrictions (AREAER) and do not represent the views of the IMF, its Executive Board, or IMF Management.*

---

## Table of Contents

- [Overview of Datasets](#overview-of-datasets)
- [Dataset Descriptions](#dataset-descriptions)
  - [iBoP-C Index](#ibop-c-index)
  - [iBoP-C Intensity Index](#ibop-c-intensity-index)
  - [iBoP-C Subcategories Index](#ibop-c-subcategories-index)
  - [Daily Policy Measures](#daily-policy-measures)
  - [iBoP-S (Stance Index)](#ibop-s-stance-index)
  - [FKRSU (LLM Extension)](#fkrsu-llm-extension)
- [File Organization](#file-organization)
- [Data Source](#data-source)
- [Methodological Notes](#methodological-notes)
- [AREAER Section References](#areaer-section-references)
- [Usage Notes](#usage-notes)
- [Citation](#citation)
- [Related Resources](#related-resources)

---

## Overview of Datasets

| Dataset | Frequency | Coverage | Description |
|---------|-----------|----------|-------------|
| **iBoP-C** | Monthly / Quarterly / Annual | 190 countries, 1950–2023 | Cumulative net tightenings of cross-border flow restrictions. |
| **iBoP-C Intensity** | Monthly / Quarterly / Annual | 190 countries, 1950–2023 | Same as iBoP-C, but weighting each policy measure by an intensity score based on a subjective assessment of the measure's economic impact on cross-border flows. |
| **iBoP-C Subcategories** | Monthly / Quarterly / Annual | 190 countries, 1950–2023 | Same as iBoP-C, but categories are further disaggregated to 24 subcategories. Intensity weighted version is available upon request. |
| **Daily Policy Measures** | Daily | 190 countries, 1950–2023 | This data provides daily information on individual policy measures. |
| **iBoP-S** | Annual | 195 countries, 1995–2023 | This data captures the overall stance of restrictions at the extensive margin. It is similar to FKRSU (LLM extension), but expanded to all eight categories of cross-border flow restrictions. Additional disaggregated subcategories are available upon request. |
| **FKRSU (LLM extension)** | Annual | 195 countries, 1995–2023 | The data expands and updates the dataset provided in Fernandez, Andres, Michael Klein, Alessandro Rebucci, Martin Schindler, and Martin Uribe, "Capital Control Measures: A New Dataset," IMF Economic Review 64, 2016, 548-574. |

---

## Dataset Descriptions

### iBoP-C Index

The change index, iBoP-C, measures changes in cross-border restrictions over time, starting from 1950 until 2023. The index relies on information from the Changes section of the AREAER, which reports changes in restrictions from all sections at the daily level starting from 1950.

After classifying these changes, our baseline measure aggregates these changes by summing all tightenings reported at the country-time-category level and subtracting all loosenings reported at the same country-time-category level. We then cumulate these net tightenings from the first year until the most recent year.

**Formula:**

For country $i$ in time $t$ and category $c$, iBoP-C is given by:

```math
iBoP\_C_{itc} = \sum_{\tau \leq t} \left( \sum_{k\in{\mathcal{T}_{i\tau c}}} Tightening_{k,i\tau c} - \sum_{l\in{\mathcal{L}_{i\tau c}}} Loosening_{l,i\tau c} \right)
```

where $Tightening_{k,itc}$ is the $k$ change that tightens restrictions in country $i$, category $c$ and time $t$, and similarly $Loosening_{l,itc}$ is the $l$ change that loosens restrictions in country $i$, category $c$ and time $t$. The sets of measures are captured in $\mathcal{T}$ and $\mathcal{L}$, which can vary across countries, time, and category.

While we report results at the annual frequency, we also provide indices at quarterly and monthly levels.

**Excel file:** 
- `excel_files/BFTU_iBoPC.xlsx`

**Stata files:**
- `stata_files/BFTU_iBoPC_Annual.dta`
- `stata_files/BFTU_iBoPC_Quarterly.dta`
- `stata_files/BFTU_iBoPC_Monthly.dta`

#### Variable Definitions for iBoP-C

| Variable | Description |
|----------|-------------|
| `total` | Cumulative number of net tightening measures across all eight categories (c1-c8). |
| `total_in` | Cumulative number of inflow-related net tightening measures across all eight categories (c1-c8). |
| `total_out` | Cumulative number of outflow-related net tightening measures across all eight categories (c1-c8). |
| `total_neutral` | Cumulative number of neutral net tightening measures across all eight categories (c1-c8). |
| `c1.fx_markets` | Cumulative number of net tightening measures related to foreign exchange markets. These include exchange restrictions and multiple currency practices maintained by a member country, foreign exchange transactions subject to a special tax, fees, or other mandatory cost, and foreign exchange transactions subsidized using separate, non-market exchange rates. We exclude measures related to exchange rate arrangements or monetary policy frameworks. These correspond to Sections II.A and III.F-H in the 2023 AREAERs. |
| `c2.payments_and_receipts` | Cumulative number of net tightening measures related to arrangements for payments and receipts. These include official requirements affecting the selection of currency and the method of settlement for transactions with other countries, agreements that prescribe specific rules for payments to each other, including cases in which private parties are also obligated to use specific currencies, separate rules for trading in gold with foreign countries, and regulations governing the physical movement of means of payment between countries. We exclude policies related to the use of foreign exchange among residents, the administration of control, and controls on domestic ownership of currency and gold. These correspond to Section IV in the 2023 AREAERs. |
| `c3.residency_accounts` | Cumulative number of net tightening measures related to residents and non-residents accounts. Policies on resident and non-resident accounts include controls on whether resident accounts that are maintained in the national currency or in foreign currency abroad are allowed, the facilities and limitations attached to these resident accounts, controls on whether local nonresident accounts maintained in the national currency or in foreign currency are allowed and the facilities and limitations attached to these non-resident accounts. We exclude restrictions on resident accounts held domestically. These correspond to Section V and VI in the 2023 AREAERs. |
| `c4.import_payments` | Cumulative number of net tightening measures related to import payments. These include restrictions on foreign exchange budgets, financing requirements of imports, and documentation requirements for the release of foreign exchange for imports. We exclude restrictions that directly impact the trade of goods and services (e.g., import licenses, taxes, and tariffs). These correspond to Section VII in the 2023 AREAERs. |
| `c5.export_proceeds` | Cumulative number of net tightening measures related to export proceeds. These include repatriation and surrender requirements for exporters, export financing requirements, and export documentation requirements. We exclude restrictions that directly impact the trade of goods and services (e.g., export licenses and taxes). These correspond to Section VII in the 2023 AREAERs. |
| `c6.invisibles` | Cumulative number of net tightening measures related to invisible transactions (payments and receipts) and current transfers. These include procedures for effecting payments abroad in connection with current transactions in invisibles, with reference to prior approval requirements, the existence of quantitative and indicative limits, and/or bona fide tests, and regulations governing exchange receipts derived from transactions in invisibles, including descriptions of any limitations on their conversion into domestic currency and the use of those receipts. These correspond to Sections IX and X in the 2023 AREAERs. |
| `c7.capital_account` | Cumulative number of net tightening measures related to capital account transactions. These include repatriation and surrender requirements, controls on capital and money market securities, controls on credit operations, controls on direct investment, controls on real estate transactions, and controls on personal capital transactions. These correspond to Section XI in the 2023 AREAERs. |
| `c8.financial_sector` | Cumulative number of net tightening measures related to the financial sector. These include regulations specific to commercial banks and other credit institutions, such as monetary, prudential, and FX market restrictions, controls specific to institutions, such as insurance companies, pension funds, investment firms (including brokers, dealers, or advisory firms), and other securities firms (including collective investment funds). When classifying restrictions in this category we include those that pertain to cross-border flows, and exclude primarily *domestic* macro-prudential policy measures, including restrictions on local FX lending, purchases of locally issued securities, treatment of FX deposit accounts, reserve requirements, liquid asset requirements, interest rate controls, and credit controls. These correspond to Section XII in the 2023 AREAERs. |

---

### iBoP-C Intensity Index

The iBoP-C Intensity Index extends the baseline iBoP-C measure by allowing each change in cross-border restrictions to have a different impact depending on its subjectively assessed severity. As with the baseline index, this measure draws on the Changes section of the AREAER, which documents daily changes to cross-border restrictions by country and categories from 1950 to present.

After classifying changes into tightenings and loosenings, each measure is assigned an intensity score $\alpha \in \{0.1, 0.25, 0.5, 0.75, 1\}$. These scores reflect the scope and nature of the measure, with higher values corresponding to measures judged to have larger economic impacts on cross-border flows.

**Formula:**

For country $i$ in time $t$ and category $c$, iBoP-C Intensity is given by:

```math
iBoP\_C_{itc}^{Int} = \sum_{\tau \leq t} \left( \sum_{k\in{\mathcal{T}_{i\tau c}}} \alpha_{k,i\tau c} \cdot Tightening_{k,i\tau c} - \sum_{l\in{\mathcal{L}_{i\tau c}}} \alpha_{l,i\tau c} \cdot Loosening_{l,i\tau c} \right)
```

where $\alpha_{k,i\tau c}$ and $\alpha_{l,i\tau c}$ are the intensity weights assigned to tightening $k$ and loosening $l$ respectively.

As with the baseline measure, we report results at annual, quarterly, and monthly frequencies.

**Excel file:** 
- `excel_files/BFTU_iBoPC_Intensity.xlsx`


**Stata files:**
- `stata_files/BFTU_iBoPC_Intensity_Annual.dta`
- `stata_files/BFTU_iBoPC_Intensity_Quarterly.dta`
- `stata_files/BFTU_iBoPC_Intensity_Monthly.dta`

**Variable definitions:** Same as iBoP-C Index (see above).

---

### iBoP-C Subcategories Index

The iBoP-C Subcategories Index further extends the baseline iBoP-C measure to 24 subcategories. This disaggregated index takes advantage of the more granular classifications of the Changes section in the AREAERs. While the AREAER began reporting these granular categories from 1999, measures in the Changes section have only been classified along these granular categories starting from 2016. We employ our ML methodology to extend these classifications for all measures reported in the Changes section back to 1950.

**Excel file:** 
- `excel_files/BTFU_iBoPC_Subcategories.xlsx`

**Stata files:**
- `stata_files/BTFU_iBoPC_Subcategories_Annual.dta`
- `stata_files/BTFU_iBoPC_Subcategories_Quarterly.dta`
- `stata_files/BTFU_iBoPC_Subcategories_Monthly.dta`

#### Variable Definitions for iBoP-C Subcategories

| Variable | Description |
|----------|-------------|
| `total` | Cumulative number of net tightening measures across all subcategories. |
| `total_in` | Cumulative number of inflow-related net tightening measures across all subcategories. |
| `total_out` | Cumulative number of outflow-related net tightening measures across all subcategories. |
| `total_neutral` | Cumulative number of neutral net tightening measures across all subcategories. |
| **Category 1: Foreign Exchange Markets** | |
| `c1.taxes_subsidies` | Cumulative number of net tightening measures related to exchange taxes and subsidies. These correspond to Sections II.A and III.F-G in the 2023 AREAERs. |
| `c1.regulations` | Cumulative number of net tightening measures related to FX market restrictions. These correspond to Section III.H in the 2023 AREAERs. |
| **Category 2: Arrangements for Payments and Receipts** | |
| `c2.currency_prescriptions` | Cumulative number of net tightening measures related to the prescription of currency requirements and bilateral payment arrangements. This corresponds to Sections IV.A-B and D in the 2023 AREAERs. |
| `c2.gold_trade` | Cumulative number of net tightening measures related to the trade of gold. This corresponds to Section IV.E in the 2023 AREAERs. |
| `c2.banknote_controls` | Cumulative number of net tightening measures related to banknotes. This corresponds to Section IV.F in the 2023 AREAERs. |
| **Category 3: Resident and Non-Resident Accounts** | |
| `c3.residents` | Cumulative number of net tightening measures related to resident accounts. This corresponds to Section V in the 2023 AREAERs. |
| `c3.nonresidents` | Cumulative number of net tightening measures related to non-resident accounts. This corresponds to Section VI in the 2023 AREAERs. |
| **Category 4: Import Payments** | |
| `c4.financing_requirements` | Cumulative number of net tightening measures related to import financing requirements. This corresponds to Section VII.A-B in the 2023 AREAERs. |
| `c4.documentation_requirements` | Cumulative number of net tightening measures related to import documentation requirements. This corresponds to Section VII.C in the 2023 AREAERs. |
| **Category 5: Export Proceeds** | |
| `c5.repatriation_and_surrender` | Cumulative number of net tightening measures related to repatriation and surrender requirements of export proceeds. This corresponds to Section VIII.A in the 2023 AREAERs. |
| `c5.financing_and_documentation_requirements` | Cumulative number of net tightening measures related to financing and documentation requirements of exports. This corresponds to Section VIII.B-C in the 2023 AREAERs. |
| **Category 6: Invisible Transactions and Current Transfers** | |
| `c6.trade_and_investments` | Cumulative number of net tightening measures related to trade and investment-related invisible payments and current transfers. This corresponds to Sections IX.A.1-2 in the 2023 AREAERs. |
| `c6.travel_and_personal` | Cumulative number of net tightening measures related to travel and personal-related invisible payments and current transfers. This corresponds to Sections IX.A.3-6 in the 2023 AREAERs. |
| `c6.repatriation_and_surrender` | Cumulative number of net tightening measures related to repatriation and surrender requirements of invisible proceeds. This corresponds to Section X in the 2023 AREAERs. |
| **Category 7: Capital Account Transactions** | |
| `c7.repatriation_and_surrender` | Cumulative number of net tightening measures related to the repatriation and surrender requirements of capital account transactions. |
| `c7.capital_and_money_market` | Cumulative number of net tightening measures related to capital and money market securities. This corresponds to Section XI.A.1-3 in the 2023 AREAERs. |
| `c7.credit_operations` | Cumulative number of net tightening measures related to credit operations. This corresponds to Section XI.A.4 in the 2023 AREAERs. |
| `c7.direct_investment` | Cumulative number of net tightening measures related to direct investments. This corresponds to Section XI.A.5-6 in the 2023 AREAERs. |
| `c7.real_estate` | Cumulative number of net tightening measures related to real estate transactions. This corresponds to Section XI.A.7 in the 2023 AREAERs. |
| `c7.personal_capital` | Cumulative number of net tightening measures related to personal capital transactions. This corresponds to Section XI.A.8 in the 2023 AREAERs. |
| **Category 8: Financial Sector** | |
| `c8.commercial_banks` | Cumulative number of net tightening measures specific to commercial banks. This corresponds to Section XII.A in the 2023 AREAERs. |
| `c8.institutional_investors` | Cumulative number of net tightening measures specific to insurance companies. This corresponds to Section XII.B.1 in the 2023 AREAERs. |
| `c8.pension_funds` | Cumulative number of net tightening measures specific to pension funds. This corresponds to Section XII.B.2 in the 2023 AREAERs. |
| `c8.collective_investment_funds` | Cumulative number of net tightening measures specific to investment firms and collective investment funds. This corresponds to Section XII.B.3 in the 2023 AREAERs. |

---

### Daily Policy Measures

This dataset contains the individual policy measures used in the construction of the iBoP-C and iBoP-C Intensity indices. Each measure is associated with several labels constructed using the LLM methodology outlined in the paper. The dataset includes the implementation date, category of restriction, direction of change (whether the policy tightened or loosened restrictions), an intensity-weighted measure of each policy, whether restrictions are being applied to inflows or outflows, and type of restriction implemented (price-based, quantity-based, or administrative).

The dataset also contains duplicate markers to indicate identical narratives within a given country-date. Users of the dataset can choose whether or not to keep these duplicated values or just unique ones.

**Excel file:** 
- `excel_files/BFTU_Daily_Policy_Measures.xlsx`

**Stata file:**
- `stata_files/BFTU_Daily_Policy_Measures.dta`

#### Variable List for Daily Policy Measures

| Variable | Description |
|----------|-------------|
| `master_index` | Unique identifier |
| `c1.fx_markets` | Policies related to foreign exchange market |
| `c2.payments_and_receipts` | Policies related to arrangements for payments and receipts |
| `c3.residency_accounts` | Policies related to resident and non-resident accounts |
| `c4.import_payments` | Policies related to import payments |
| `c5.export_proceeds` | Policies related to export proceeds |
| `c6.invisibles` | Policies related to invisible transactions and current transfers |
| `c7.capital_account` | Policies related to capital account transactions |
| `c8.financial_sector` | Policies related to financial sector regulations |
| `direction` | Direction of change (whether the policy tightened or loosened restrictions) |
| `intensity` | Intensity-weighted score of each policy, α, based on the scope and nature of the measure |
| `flow` | Type of restriction implemented (outflow-oriented or inflow-oriented) |
| `price` | Type of restriction implemented (price-based, quantity-based, and/or administrative) |
| `duplicated_id` | Identical narratives share the same duplicate ID |

---

### iBoP-S (Stance Index)

The stance index, iBoP-S, summarizes the level of cross-border restrictions in place for each country-year-category, based on the stance information provided in the AREAER. In contrast to iBoP-C, which relies on daily changes, the iBoP-S identifies the existence of restrictions for each subcategory reported in the AREAER stance sections. These granular classifications are available starting from 1995.

A key feature of the iBoP-S construction is that it respects the hierarchical structure of the AREAER. The AREAER organizes restrictions in a nested taxonomy: broad categories (e.g., capital and money market instruments) contain subcategories (e.g., equity inflows and outflows), which themselves contain more granular subcategories (e.g., equity purchases by non-residents and equity sales by residents abroad). The stance index mirrors this structure and is constructed using a bottom-up approach.

At the lowest level, each subcategory $s$ is a binary indicator $\mathcal{I}_{s,it} \in \{0,1\}$, with 1 indicating that a restriction exists and 0 indicating that no or minimal restrictions exist. Intermediate parent categories aggregate their children categories by taking a simple average of the stance indicators of all nodes directly below them. Missing values or non-numerical values are ignored in computing the averages. Higher-level categories aggregate the stance values of their immediate children categories in the same way.

**Formula:**

Let the AREAER define a hierarchy for each category $c$, where every node $n$ has a set of immediate child nodes $\mathcal{C}(n)$. The stance value for any node is defined recursively as:

```math
Stance_{it}(n) = \begin{cases}
    \mathcal{I}_{n,it}, & \text{if } \mathcal{C}(n) = \varnothing \\[6pt]
    \displaystyle \frac{1}{|\mathcal{C}(n)|} \sum_{m \in \mathcal{C}(n)} Stance_{it}(m), & \text{if } \mathcal{C}(n) \neq \varnothing
\end{cases}
```

The stance index for a top-level AREAER category $c$ (the same eight categories used in the iBoP-C index) for country $i$ in year $t$ is then defined as:

```math
iBoP\_S_{itc} = Stance_{it}(c)
```

Thus, the value of each category is an equally weighted average over all subcomponents, where weights arise naturally from the nested structure of the taxonomy. Unlike the iBoP-C, iBoP-S index is available only at the annual frequency, because the stance of restrictions is reported annually in the AREAER.

**Excel file:** 
- `excel_files/BFTU_iBoPS.xlsx`

**Stata file:**
- `stata_files/BFTU_iBoPS.dta`

#### Variable Definitions for iBoP-S

| Variable | Description |
|----------|-------------|
| `total` | Average stance across all eight categories. |
| `total_in` | Average stance across inflow-related subcategories within each of the eight categories (c1-c8). |
| `total_out` | Average stance across outflow-related subcategories within each of the eight categories (c1-c8). |
| `total_neutral` | Average stance across neutral subcategories within each of the eight categories (c1-c8). |
| `c1.fx_markets` | Average stance of restrictions related to foreign exchange markets. |
| `c2.payments_and_receipts` | Average stance of restrictions related to arrangements for payments and receipts. |
| `c3.residency_accounts` | Average stance of restrictions related to residents and non-residents accounts. |
| `c4.import_payments` | Average stance of restrictions related to import payments. |
| `c5.export_proceeds` | Average stance of restrictions related to export proceeds. |
| `c6.invisibles` | Average stance of restrictions related to invisible transactions (payments and receipts) and current transfers. |
| `c7.capital_account` | Average stance of restrictions related to capital account transactions. |
| `c8.financial_sector` | Average stance of restrictions related to the financial sector. |

---

### FKRSU (LLM Extension)

The FKRSU index focuses on the overall stance of capital account restrictions (ka) and their inflow (kai) and outflow (kao) components. These indices are composed of 32 subcategories, covering 6 types of instruments: capital and money market securities, collective investment securities, derivatives, credit operations, direct investment, and real estate.

This index replicates and expands upon Fernandez et al. (2016) using our LLM-based approach. While the original FKRSU index covers 100 countries from 1995 to 2019, this index expands coverage until 2023 for 195 countries.

**Excel file:** 
- `excel_files/FKRSU_LLM.xlsx`

**Stata file:**
- `stata_files/FKRSU_LLM.dta`

#### Variable Definitions for FKRSU

| Variable | Description | Formula |
|----------|-------------|---------|
| `ka` | Overall restrictions index (all asset categories) | Average(kai, kao) |
| `kai` | Overall inflow restrictions index (all asset categories) | Average(eqi, boi, mmi, cii, dei, cci, fci, gsi, dii, rei) |
| `kao` | Overall outflow restrictions index (all asset categories) | Average(eqo, boo, mmo, cio, deo, cco, fco, gso, dio, reo) |
| **Equity** | | |
| `eq` | Average equity restrictions | Average(eqi, eqo) |
| `eqi` | Equity inflow restrictions | Average(eq_plbn, eq_siar) |
| `eqo` | Equity outflow restrictions | Average(eq_siln, eq_pabr) |
| `eq_plbn` | Purchase locally by nonresidents (equity) | |
| `eq_siln` | Sale or issue locally by nonresidents (equity) | |
| `eq_pabr` | Purchase abroad by residents (equity) | |
| `eq_siar` | Sale or issue abroad by residents (equity) | |
| **Bonds** | | |
| `bo` | Average bond restrictions | Average(boi, boo) |
| `boi` | Bond inflow restrictions | Average(bo_plbn, bo_siar) |
| `boo` | Bond outflow restrictions | Average(bo_siln, bo_pabr) |
| `bo_plbn` | Purchase locally by nonresidents (bonds) | |
| `bo_siln` | Sale or issue locally by nonresidents (bonds) | |
| `bo_pabr` | Purchase abroad by residents (bonds) | |
| `bo_siar` | Sale or issue abroad by residents (bonds) | |
| **Money Market** | | |
| `mm` | Average money market restrictions | Average(mmi, mmo) |
| `mmi` | Money market inflow restrictions | Average(mm_plbn, mm_siar) |
| `mmo` | Money market outflow restrictions | Average(mm_siln, mm_pabr) |
| `mm_plbn` | Purchase locally by nonresidents (money market instruments) | |
| `mm_siln` | Sale or issue locally by nonresidents (money market instruments) | |
| `mm_pabr` | Purchase abroad by residents (money market instruments) | |
| `mm_siar` | Sale or issue abroad by residents (money market instruments) | |
| **Collective Investments** | | |
| `ci` | Average collective investments restrictions | Average(cii, cio) |
| `cii` | Collective investments inflow restrictions | Average(ci_plbn, ci_siar) |
| `cio` | Collective investments outflow restrictions | Average(ci_siln, ci_pabr) |
| `ci_plbn` | Purchase locally by nonresidents (collective investments) | |
| `ci_siln` | Sale or issue locally by nonresidents (collective investments) | |
| `ci_pabr` | Purchase abroad by residents (collective investments) | |
| `ci_siar` | Sale or issue abroad by residents (collective investments) | |
| **Derivatives** | | |
| `de` | Average derivatives restrictions | Average(dei, deo) |
| `dei` | Derivatives inflow restrictions | Average(de_plbn, de_siar) |
| `deo` | Derivatives outflow restrictions | Average(de_siln, de_pabr) |
| `de_plbn` | Purchase locally by nonresidents (derivatives) | |
| `de_siln` | Sale or issue locally by nonresidents (derivatives) | |
| `de_pabr` | Purchase abroad by residents (derivatives) | |
| `de_siar` | Sale or issue abroad by residents (derivatives) | |
| **Credit Operations** | | |
| `cc` | Average commercial credits restrictions | Average(cci, cco) |
| `cci` | Commercial credits inflow restrictions | |
| `cco` | Commercial credits outflow restrictions | |
| `fc` | Average financial credits restrictions | Average(fci, fco) |
| `fci` | Financial credits inflow restrictions | |
| `fco` | Financial credits outflow restrictions | |
| `gs` | Average guarantees, sureties and financial backup facilities restrictions | Average(gsi, gso) |
| `gsi` | Guarantees, sureties and financial backup facilities inflow restrictions | |
| `gso` | Guarantees, sureties and financial backup facilities outflow restrictions | |
| **Direct Investment** | | |
| `di` | Average direct investment restrictions | Average(dii, dio) |
| `dii` | Direct investment inflow restrictions | |
| `dio` | Direct investment outflow restrictions | |
| `ldi` | Direct investment liquidation restrictions | |
| **Real Estate** | | |
| `re` | Average real estate restrictions | Average(rei, reo) |
| `rei` | Real estate inflow restrictions | re_plbn |
| `reo` | Real estate outflow restrictions | Average(re_pabr, re_slbn) |
| `re_pabr` | Purchase abroad by residents (real estate) | |
| `re_plbn` | Purchase locally by nonresidents (real estate) | |
| `re_slbn` | Sale locally by nonresidents (real estate) | |

---

## File Organization

```
├── excel_files/
│   ├── BFTU_Daily_Policy_Measures.xlsx
│   ├── BFTU_iBoPC.xlsx
│   ├── BFTU_iBoPC_Intensity.xlsx
│   ├── BFTU_iBoPS.xlsx
│   ├── BTFU_iBoPC_Subcategories.xlsx
│   └── FKRSU_LLM.xlsx
└── stata_files/
    ├── BFTU_Daily_Policy_Measures.dta
    ├── BFTU_iBoPC_Annual.dta
    ├── BFTU_iBoPC_Monthly.dta
    ├── BFTU_iBoPC_Quarterly.dta
    ├── BFTU_iBoPC_Intensity_Annual.dta
    ├── BFTU_iBoPC_Intensity_Monthly.dta
    ├── BFTU_iBoPC_Intensity_Quarterly.dta
    ├── BFTU_iBoPS.dta
    ├── BTFU_iBoPC_Subcategories_Annual.dta
    ├── BTFU_iBoPC_Subcategories_Monthly.dta
    ├── BTFU_iBoPC_Subcategories_Quarterly.dta
    └── FKRSU_LLM.dta
```

---

## Data Source

All datasets are derived from the **IMF's Annual Report on Exchange Rate Arrangements and Restrictions (AREAER)**, which reports daily changes in restrictions starting from 1950.

- **Coverage**: Up to 195 countries
- **Time period**: 1950–2023 (varies by dataset)
- **Update frequency**: The AREAER is published annually

---

## Methodological Notes

### LLM-Based Classification
The datasets employ Large Language Model (LLM) methodology to classify and extend historical data. This allows for:
- Consistent classification of policy measures across time
- Extension of granular subcategory classifications back to 1950
- Expansion of the original FKRSU dataset

### Eight Main Categories of Restrictions

1. **Foreign Exchange Markets** (c1)
2. **Arrangements for Payments and Receipts** (c2)
3. **Resident and Non-Resident Accounts** (c3)
4. **Import Payments** (c4)
5. **Export Proceeds** (c5)
6. **Invisible Transactions and Current Transfers** (c6)
7. **Capital Account Transactions** (c7)
8. **Financial Sector** (c8)

### Intensity Scoring

Policy measures are assigned intensity scores based on their assessed economic impact:

| Score | Interpretation |
|-------|----------------|
| 0.1 | When a notification or documentation requirement is needed |
| 0.25 | When a tax is levied |
| 0.5 | When a quantitative limit is imposed |
| 0.75 | When an approval is required |
| 1.0 | When a ban exists |

### Flow Direction Classification

Policies are classified by their target:
- **Inflows**: Restrictions on incoming cross-border flows
- **Outflows**: Restrictions on outgoing cross-border flows
- **Neutral**: Restrictions that apply to both or neither direction

### Restriction Types

Policies are categorized by implementation method:
- **Price-based**: Taxes, fees, or other cost-based measures
- **Quantity-based**: Quotas, limits, or caps on volumes
- **Administrative**: Approval requirements, documentation, or procedural restrictions

### Hierarchical Aggregation (iBoP-S and FKRSU)

These indices use bottom-up hierarchical aggregation:
- Leaf nodes are binary (0 = no restriction, 1 = restriction exists)
- Parent nodes are simple averages of child nodes
- Values range from 0 (fully open) to 1 (fully restricted)

---

## AREAER Section References

The following table maps the eight main categories to their corresponding sections in the 2023 AREAER:

| Category | AREAER Sections (2023) |
|----------|------------------------|
| **C1: Foreign Exchange Markets** | II.A, III.F-H |
| **C2: Arrangements for Payments and Receipts** | IV |
| **C3: Resident and Non-Resident Accounts** | V, VI |
| **C4: Import Payments** | VII (import-related) |
| **C5: Export Proceeds** | VIII |
| **C6: Invisible Transactions and Current Transfers** | IX, X |
| **C7: Capital Account Transactions** | XI |
| **C8: Financial Sector** | XII |

---

## Usage Notes

### Loading the Data

**Excel Files:**
```python
import pandas as pd

# Load iBoP-C index
ibopc = pd.read_excel('excel_files/BFTU_iBoPC.xlsx')

# Load daily policy measures
daily = pd.read_excel('excel_files/BFTU_Daily_Policy_Measures.xlsx')
```

**Stata Files:**
```stata
* Load annual iBoP-C data
use "stata_files/BFTU_iBoPC_Annual.dta", clear

* Load monthly iBoP-C Intensity data
use "stata_files/BFTU_iBoPC_Intensity_Monthly.dta", clear
```

### Variable Naming Conventions

- **Category prefixes**: `c1` through `c8` indicate the eight main categories
- **Flow suffixes**: `_in` (inflows), `_out` (outflows), `_neutral` (neutral/both)

### Treatment of Duplicates

The Daily Policy Measures dataset includes a `duplicated_id` field that identifies identical policy narratives within the same country-date. Users can choose to:
- **Keep duplicates**: Use all observations to capture the full reporting structure
- **Remove duplicates**: Filter to unique narratives using the `duplicated_id` field

### Additional Data

The following data are available upon request:
- Intensity-weighted version of iBoP-C Subcategories
- Additional disaggregated subcategories for iBoP-S
- Extended time series or country coverage (subject to data availability)

---

## Citation

If you use this data, please cite:

```
Bergant, Katharina, Andrés Fernández, Ken Teoh, and Martín Uribe. 2025.
"Expanding the Landscape of Cross-Border Flow Restrictions: Modern Tools and Historical Perspectives"
```

For the original FKRSU dataset, also cite:

```
Fernandez, Andres, Michael Klein, Alessandro Rebucci, Martin Schindler, and Martin Uribe. 2016.
"Capital Control Measures: A New Dataset"
IMF Economic Review 64, 548-574.
```

---

## Related Resources

- **BTFU Data Dashboard**: [Data Dashboard](https://b855d13c-a1b6-427a-915d-f5205a569bf6.plotly.app)
- **IMF AREAER**: [https://www.imf.org/en/Publications/Annual-Report-on-Exchange-Arrangements-and-Exchange-Restrictions](https://www.imf.org/en/Publications/Annual-Report-on-Exchange-Arrangements-and-Exchange-Restrictions)

---

## Contact

For questions, comments, or data requests, please contact the authors:

- **Katharina Bergant** - kbergant@imf.org
- **Andrés Fernández** - afernandez3@imf.org
- **Ken Teoh** - hteoh@imf.org
- **Martín Uribe** - mu2166@columbia.edu

---

**Last Updated**: December 2025
