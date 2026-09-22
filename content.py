"""
Site content — everything the pages render, in one place.

Two identities share a person: the accent colour, copy, experience framing and
project set all swap between them. Facts stay constant; only emphasis moves.
Source of truth for experience wording is the canonical resume set in
~/Desktop/Simon Job Search 2026/01 Base Resumes/00 Canonical Bases.
"""

BASE = "/Users/7ang/Desktop/Github Academic Project"

SHARED = dict(
    name="Simon Chen",
    email="xingyang@marshall.usc.edu",
    phone="(949) 591-3777",
    location="Los Angeles, CA",
    linkedin="https://www.linkedin.com/in/simonxy-chen",
    github="https://github.com/Semin1c",
    education=[
        dict(school="University of Southern California, Marshall School of Business",
             place="Los Angeles, CA", date="May 2026",
             degree="Master of Science in Business Analytics (STEM)",
             note="GPA 3.78 · Dean's Honor List, 3 semesters"),
        dict(school="University of California, Irvine", place="Irvine, CA", date="June 2024",
             degree="Bachelor of Arts in Business Economics, Minor in Management",
             note="GPA 3.92 · Dean's Honor List, 9 quarters · Phi Beta Kappa"),
    ],
)

MODES = {
"analyst": dict(
    key="analyst", label="Data / Business", accent="#990000", gold="#FFCC00",
    school="USC", eyebrow="Data &amp; Business Analytics",
    headline="I find the number that changes the decision.",
    lede="Master's in Business Analytics at USC Marshall. I build the pipeline, run the model, "
         "then spend most of my time trying to break the answer before someone spends money on it.",
    nav_tag="Data &amp; Business Analytics",

    about_title="Analytics that survives being checked",
    about=[
        "Most analysis fails quietly. The model scores well, the deck gets approved, and nobody "
        "notices the number was measuring the wrong thing. I've found that in my own work often "
        "enough that checking it has become the habit rather than the afterthought.",
        "A retention program I'd sized at a 13x return came back closer to 1.2x once the costs "
        "were built from the actual headcount instead of an industry benchmark. A claim-status "
        "model scoring 0.83 AUC turned out to be predicting whether someone had <em>ever</em> "
        "filed a claim, not whether they would this year. Both were mine to catch.",
        "That's the part I'd want a team to hire. Producing a number is straightforward. Knowing "
        "whether it holds up is the job.",
    ],
    about_kicker="What I work on",
    about_list=[
        ("Churn and retention", "Who leaves, what actually drives it, and what keeping them is worth."),
        ("Pricing and risk", "Loss modelling on heavily skewed distributions where the average is useless."),
        ("BI and reporting", "Power BI dashboards with what-if scenarios that survive contact with a real budget."),
        ("Data pipelines", "Multi-source ingestion, ID matching, and validation that runs without babysitting."),
    ],

    xp_title="Where I've done this",
    experience=[
        dict(org="Excel Sports Management", place="Irvine, CA", date="June 2025 – August 2025",
             role="Sports Performance Associate, Analytics", bullets=[
             "Built and validated an R/Python pipeline integrating 5+ data sources and APIs, automating extraction, cleaning, ID matching, metrics and reporting for 200+ athletes to cut recurring work by roughly 80%",
             "Applied regression and clustering to performance data, turning behavioural patterns into athlete profiles that informed individualised training and monitoring decisions",
             "Built R Shiny and Streamlit tools retained by the performance team, integrating performance, body-composition, nutrition and well-being data to support 3–10 weekly athlete reviews",
             ]),
        dict(org="Trojans Sports Research Lab", place="Los Angeles, CA", date="January 2025 – Present",
             role="Program & Project Manager", bullets=[
             "Led hands-on Python and SQL analysis across performance, workload and demographic datasets, converting multi-source findings into decision-ready insights for research and operations stakeholders",
             "Created reusable data-collection standards, templates, an illustrated guide and a recorded tutorial for 30+ members, clarifying field, quality and delivery requirements",
             "Directed 5+ research and analytics projects of 5–10 members each while coordinating roughly 50 core contributors inside a 200+ member lab",
             ]),
        dict(org="China Merchants Securities Co., Ltd", place="Beijing, China", date="April 2023 – August 2023",
             role="Investment Banking Department Analyst Intern", bullets=[
             "Analysed 2020–2023 financial and operating data for eight companies, then deep-dived two groups' support for subsidiary listings and their business, resource and capital synergies",
             "Revised 2–3 client-facing convertible-bond and refinancing proposals, reconciling financial tables, company profiles, risk factors and financing logic; the changes carried into later review versions",
             ]),
    ],

    proj_title="Three that show the range",
    proj_lede="Churn, workforce economics, and the dashboard that talked a budget out of being spent.",
    projects=[
        dict(tag="Churn · Streaming", title="Netflix Subscriber Churn",
             stat="5,000", label="subscribers modelled",
             desc="Engagement is the only driver that matters. Strip viewing behaviour out and three "
                  "different classifiers collapse to barely better than a coin flip.",
             body="Across 5,000 subscribers, how much someone watches separates churners from stayers "
                  "so cleanly that everything else is noise. The retention play targets disengaged "
                  "Basic-plan subscribers specifically, because that's where spend has somewhere to go.",
             fig=f"{BASE}/MKT 566 - Netflix Churn Prediction (2025 Fall)/Git Version/figures/churn_by_engagement.png",
             repo="https://github.com/Semin1c/netflix-churn-engagement", stack="Python · scikit-learn · XGBoost"),
        dict(tag="People analytics · ROI", title="Employee Attrition & Retention ROI",
             stat="0.85", label="held-out ROC-AUC",
             desc="Attrition concentrates hard enough that two segments cover a third of departures "
                  "across a tenth of the workforce. The honest ROI is a fraction of the headline one.",
             body="1,470 employees, 31 features, regularised logistic regression. Business travel, "
                  "overtime and promotion timing carry the signal. Turning risk scores into a "
                  "156-employee pilot covers 35% of predicted departures — and re-costing the programme "
                  "per employee and per role replaced a benchmark-driven 13x with a defensible $83K.",
             fig=f"{BASE}/DSO 550 - IBM Employee Attrition ROI (2026 Spring)/Git Version/outputs/figures/exec/step3_segment_playbook_onepager.png",
             repo="https://github.com/Semin1c/ibm-attrition-roi", stack="Python · scikit-learn · statsmodels"),
        dict(tag="BI · What-if modelling", title="Sales Performance Dashboards",
             stat="−15%", label="ROI on the training everyone wanted",
             desc="Three Power BI dashboards on a $25.7M book, tracing a question from \"how are we "
                  "doing\" to \"what should we fund\" — and finding the obvious answer loses money.",
             body="Training looks like a driver in a decomposition tree, so the instinct is to fund it. "
                  "Tested directly, rep attributes correlate near zero with sales per rep. What "
                  "separates reps is who they report to — a $134K supervisor gap. Both costings of the "
                  "training programme come back negative.",
             fig=f"{BASE}/DSO 550 - People Analytics Power BI Dashboards (2026 Spring)/Git Version/figures/what_actually_drives_sales.png",
             repo="https://github.com/Semin1c/people-analytics-dashboards", stack="Power BI · DAX · What-if parameters"),
    ],
    skills=[
        ("Analytics & modelling", "SQL · Python · R · Regression · Classification · Clustering · Forecasting · A/B testing"),
        ("BI & reporting", "Power BI · Tableau · R Shiny · Streamlit · Excel · KPI development"),
        ("Data & platforms", "PostgreSQL · ETL · APIs · Data modelling · Data quality · Git/GitHub"),
        ("Languages", "English and Chinese (bilingual) · Spanish (intermediate)"),
    ],
    contact_title="Open to analyst roles",
    contact_lede="Looking for data and business analyst positions, starting May 2026. "
                 "Email is the fastest way to reach me.",
),

"sports": dict(
    key="sports", label="Sports", accent="#0064A4", gold="#FFD200",
    school="UC Irvine", eyebrow="Sports Analytics",
    headline="Most of what we &ldquo;know&rdquo; about football doesn't survive a test.",
    lede="Master's in Business Analytics at USC Marshall, with two seasons of work inside sports "
         "performance. I test the claims everyone repeats — possession, home advantage, competitive "
         "balance — and they usually don't hold.",
    nav_tag="Sports Analytics",

    about_title="Testing the things everyone assumes",
    about=[
        "Football analysis is full of claims nobody checks. Possession wins matches. The crowd drives "
        "home advantage. Europe's big five are more competitive than MLS. Each is testable, and each "
        "one weakens or reverses when you actually run it.",
        "My own work included. One project started from an assumption printed on slide two of the "
        "original deck — that European leagues are inherently more competitive. I coded it straight "
        "into the target variable, then went back, tested it properly, and found the data said the "
        "opposite. The accuracy figure I'd reported was riding an 85.6% majority class.",
        "Alongside that, two seasons inside sports performance: athlete pipelines, readiness "
        "monitoring, and tooling that coaching staff actually kept using.",
    ],
    about_kicker="What I work on",
    about_list=[
        ("Match and season analysis", "Possession, chance creation, home advantage, competitive balance."),
        ("Player and roster evaluation", "What transfers across clubs, and what was only ever context."),
        ("Athlete performance data", "Workload, readiness and testing data turned into coach-facing tools."),
        ("Schedule and travel", "Rest, compression and opponent sequencing separated from team quality."),
    ],

    xp_title="Where I've done this",
    experience=[
        dict(org="Excel Sports Management", place="Irvine, CA", date="June 2025 – August 2025",
             role="Sports Performance Associate, Analytics", bullets=[
             "Built and validated an R/Python pipeline integrating 5+ performance data sources and APIs, automating extraction, cleaning, ID matching, metrics and reporting for 200+ athletes to cut recurring work by roughly 80%",
             "Modelled relationships among neuromuscular, sprint, strength, pitch-speed and bat-speed measures, helping performance staff interpret athlete drivers and support individualised training discussions",
             "Integrated performance, body-composition, nutrition and well-being data against age- and level-based benchmarks, helping coaches identify gaps and set priorities across 3–10 weekly reviews",
             "Built R Shiny and Streamlit dashboards retained by the performance team, centralising athlete trends and readiness indicators for recurring coach-facing review",
             ]),
        dict(org="Trojans Sports Research Lab", place="Los Angeles, CA", date="January 2025 – Present",
             role="Program & Project Manager", bullets=[
             "Managed 5+ sports and analytics research projects of 5–10 members each inside a 200+ member lab, adapting assignments and timelines to keep milestones moving",
             "Created reusable data-collection standards, templates, an illustrated guide and a recorded tutorial for 30+ members, clarifying field, quality and delivery requirements",
             "Supported analysis and validation across three sports research projects, with two abstracts accepted by ACSM; presented both posters and findings on site",
             ]),
        dict(org="China Merchants Securities Co., Ltd", place="Beijing, China", date="April 2023 – August 2023",
             role="Investment Banking Department Analyst Intern", bullets=[
             "Analysed 2020–2023 financial and operating data for eight companies and deep-dived two groups' subsidiary-listing support and internal synergies to inform opportunity assessment",
             ]),
    ],

    proj_title="Four findings that reversed the assumption",
    proj_lede="Possession, home advantage, competitive balance, and what a schedule is actually worth.",
    projects=[
        dict(tag="Premier League · 8 seasons", title="Possession vs. Box Entry",
             stat="23", label="metrics beaten by one",
             desc="Possession share explains almost nothing. Touches in the box explain nearly "
                  "everything — and 22 further metrics add no information on unseen clubs.",
             body="Across 160 Premier League squad-seasons, one variable outperformed the full metric "
                  "set out of sample, which argues for a simpler chance-creation KPI than most models "
                  "use. Comparing 168 transfers against same-position benchmarks, final-third "
                  "involvement held up across clubs better than xG+xAG output did.",
             fig=f"{BASE}/DSO 579 - Premier League Possession Analysis (2025 Spring)/Git Version/figures/what_predicts_chances.png",
             repo="https://github.com/Semin1c/pl-possession-and-box-entry", stack="Python · cross-validation · recruitment analytics"),
        dict(tag="La Liga · 380 matches", title="Where Home Advantage Comes From",
             stat="p = 0.54", label="crowd effect, once quality is controlled",
             desc="The home edge is territorial, not finishing. Crowd size stops predicting anything "
                  "once you account for who fills big stadiums.",
             body="Home sides create 1.484 expected goals to 1.121 while converting at an identical "
                  "rate — so the advantage is about where the ball goes, not what happens when it "
                  "arrives. Attendance looks like an explanation until club quality is held constant. "
                  "The referee spread sits inside what random shuffling produces.",
             fig=f"{BASE}/DSO 579 - First Goal Scoring Analysis (2025 Spring)/Git Version/figures/crowd_confound.png",
             repo="https://github.com/Semin1c/laliga-home-advantage", stack="Python · permutation testing · xG"),
        dict(tag="MLS · Europe's big five", title="Competitive Balance, Reversed",
             stat="0.315", label="points-per-match spread, lowest of six",
             desc="On parity, MLS beats every one of Europe's big five — on two independent measures, "
                  "across fourteen seasons.",
             body="The project started by assuming the opposite and coding it into the target variable. "
                  "Tested properly, MLS runs the tightest spread of the six leagues while Bayern took "
                  "11 of 14 Bundesliga titles. The classifier I first reported at 88–90% accuracy was "
                  "riding an 85.6% majority class; corrected, it reaches 0.954 AUC.",
             fig=f"{BASE}/DSO 579 - MLS vs European League Analysis (2025 Spring)/Git Version/figures/competitive_balance.png",
             repo="https://github.com/Semin1c/mls-vs-european-leagues", stack="Python · scikit-learn · SHAP"),
        dict(tag="NBA · 10 seasons", title="Schedule, Travel & Rest",
             stat="~61%", label="win rate with a 2+ day rest edge",
             desc="Separating travel, rest and opponent sequencing from team quality across 300 "
                  "team-seasons, to see what the calendar is worth before a ball is thrown.",
             body="Rest advantage, back-to-backs and schedule compression translate into differences "
                  "of up to roughly five wins across a regular season — enough to matter for planning "
                  "and for reading a standings table honestly.",
             fig=None,
             repo="https://github.com/Semin1c", stack="Python · schedule modelling"),
    ],
    skills=[
        ("Analytics & modelling", "Python · SQL · R · Regression · Classification · Clustering · Time series · Predictive modelling"),
        ("Sports data", "Team & player evaluation · Match analysis · Performance & tracking data · Schedule and travel analysis"),
        ("Tooling & BI", "Power BI · Tableau · R Shiny · Streamlit · APIs · ETL · Data validation · Git/GitHub"),
        ("Languages", "English and Chinese (bilingual) · Spanish (intermediate)"),
    ],
    contact_title="Open to sports analytics roles",
    contact_lede="Looking for analyst positions with clubs, leagues and performance groups, "
                 "starting May 2026. Email is the fastest way to reach me.",
),
}
