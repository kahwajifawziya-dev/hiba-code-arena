import streamlit as st


st.set_page_config(
    page_title="Hiba's Code Arena",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded",
)


# -----------------------------------------------------------------------------
# Educational content
# -----------------------------------------------------------------------------

PAGES = ["الرئيسية", "اختبار بايثون", "تحديات تصحيح الأخطاء", "إنجازاتي", "إلى المعلمة هبة", "عن المشروع"]

QUIZ_LEVELS = {
    "مبتدئ": [
        {"question": "أي دالة نستخدمها لعرض نص على الشاشة في بايثون؟", "options": ["show()", "print()", "display_text()", "write()"], "answer": "print()", "explanation": "تُستخدم الدالة print() لعرض النصوص والقيم في وحدة الإخراج."},
        {"question": "ما الرمز الذي يبدأ به التعليق في بايثون؟", "options": ["//", "#", "<!--", "**"], "answer": "#", "explanation": "يبدأ التعليق في بايثون بالرمز #، ولا ينفّذ المفسّر ما يأتي بعده في السطر."},
        {"question": "ما نوع القيمة 'Hello'؟", "options": ["عدد صحيح", "عدد عشري", "نص (string)", "قيمة منطقية"], "answer": "نص (string)", "explanation": "علامات الاقتباس تجعل Hello نصاً من نوع string."},
        {"question": "ما ناتج التعبير 3 + 4؟", "options": ["34", "7", "12", "خطأ"], "answer": "7", "explanation": "يجمع عامل + العددين، لذلك 3 + 4 تساوي 7."},
        {"question": "كيف ننشئ متغيّراً اسمه age وقيمته 12؟", "options": ["var age = 12", "age == 12", "age = 12", "let age: 12"], "answer": "age = 12", "explanation": "في بايثون ننشئ المتغيّر بإسناد قيمة إليه باستخدام علامة =."},
    ],
    "متوسط": [
        {"question": "أي بنية تكرار تناسب المرور على عناصر قائمة؟", "options": ["for", "define", "repeat", "loopif"], "answer": "for", "explanation": "تُستخدم for للتكرار على عناصر قائمة أو أي مجموعة قابلة للتكرار."},
        {"question": "ما ناتج len([4, 8, 12])؟", "options": ["2", "3", "4", "24"], "answer": "3", "explanation": "تعيد len() عدد العناصر في القائمة، وهنا توجد ثلاثة عناصر."},
        {"question": "أي عامل نستخدم للتحقق من تساوي قيمتين؟", "options": ["=", "==", "!=", ":="], "answer": "==", "explanation": "العامل == يقارن قيمتين، أما = فيُستخدم لإسناد قيمة إلى متغيّر."},
        {"question": "ما الكلمة التي تعيد قيمة من الدالة؟", "options": ["print", "break", "return", "continue"], "answer": "return", "explanation": "تُعيد return قيمة من الدالة إلى المكان الذي استدعاها."},
        {"question": "ما الأعداد التي ينتجها range(3)؟", "options": ["1، 2، 3", "0، 1، 2", "0، 1، 2، 3", "3 فقط"], "answer": "0، 1، 2", "explanation": "تبدأ range(3) افتراضياً من 0 وتتوقف قبل 3."},
    ],
    "محترف": [
        {"question": "ما وظيفة الكلمة المفتاحية try؟", "options": ["تكرّر الأوامر دائماً", "تختبر كتلة قد ترفع استثناءً", "تنشئ قائمة", "تستورد مكتبة"], "answer": "تختبر كتلة قد ترفع استثناءً", "explanation": "تُستخدم try مع except للتعامل مع الاستثناءات المحتملة أثناء تنفيذ الكود."},
        {"question": "ما ناتج [x * 2 for x in [1, 2, 3]]؟", "options": ["[1, 2, 3]", "[2, 4, 6]", "[1, 4, 9]", "6"], "answer": "[2, 4, 6]", "explanation": "هذا تعبير list comprehension يضاعف كل عنصر في القائمة."},
        {"question": "أي عبارة تصف القاموس (dictionary)؟", "options": ["مجموعة من الأحرف فقط", "مجموعة أزواج مفتاح وقيمة", "عدد عشري", "حلقة تكرار"], "answer": "مجموعة أزواج مفتاح وقيمة", "explanation": "يخزّن القاموس البيانات كأزواج من المفاتيح والقيم، مثل {'name': 'Hiba'}."},
        {"question": "ما فائدة استخدام with عند فتح ملف؟", "options": ["يجعل الملف أكبر", "يغلق الملف تلقائياً بعد انتهاء الكتلة", "يحوّل الملف إلى قائمة", "يمنع قراءة الملف"], "answer": "يغلق الملف تلقائياً بعد انتهاء الكتلة", "explanation": "تدير with موارد الملف، وتضمن إغلاقه تلقائياً حتى لو حدث استثناء."},
        {"question": "ما المقصود بـ lambda في بايثون؟", "options": ["دالة صغيرة مجهولة الاسم", "نوع من القوائم", "تعليمة لطباعة النصوص", "حلقة لا نهائية"], "answer": "دالة صغيرة مجهولة الاسم", "explanation": "تنشئ lambda دالة قصيرة من تعبير واحد، وغالباً تستخدم للعمليات البسيطة."},
    ],
}

CHALLENGES = [
    {"title": "التحدي الأول: قوس مفقود", "description": "نريد عرض تحية على الشاشة. اكتشفي الخطأ وأصلحيه.", "code": 'print("مرحباً"', "diagnosis": "قوس إغلاق مفقود", "diagnoses": ["قوس إغلاق مفقود", "اسم الدالة مكتوب خطأ", "يجب استخدام حلقة for", "علامة الاقتباس زائدة"], "starter": 'print("مرحباً"', "required": 'print("مرحباً")', "solution": 'print("مرحباً")', "explanation": "بدأ استدعاء print بقوس مفتوح، لذلك نضيف قوساً مغلقاً في نهاية السطر."},
    {"title": "التحدي الثاني: النقطتان بعد if", "description": "يجب أن يطبع البرنامج رسالة عندما يكون العدد موجباً.", "code": "number = 5\nif number > 0\n    print('موجب')", "diagnosis": "النقطتان الرأسيتان مفقودتان بعد شرط if", "diagnoses": ["النقطتان الرأسيتان مفقودتان بعد شرط if", "المتغير يجب أن يكون نصاً", "يجب استبدال print بـ input", "يجب حذف علامة >"], "starter": "number = 5\nif number > 0\n    print('موجب')", "required": "if number > 0:", "solution": "number = 5\nif number > 0:\n    print('موجب')", "explanation": "تحتاج التعليمة الشرطية if إلى نقطتين رأسيتين في نهاية سطر الشرط."},
    {"title": "التحدي الثالث: المسافة البادئة", "description": "أصلحي المسافة البادئة حتى يصبح أمر الطباعة داخل الشرط.", "code": "number = 5\nif number > 0:\nprint('موجب')", "diagnosis": "أمر print يحتاج إلى مسافة بادئة داخل if", "diagnoses": ["أمر print يحتاج إلى مسافة بادئة داخل if", "ينقص الشرط علامة =", "اسم المتغير غير صالح", "يجب أن تكون print قبل if"], "starter": "number = 5\nif number > 0:\nprint('موجب')", "required": "    print('موجب')", "solution": "number = 5\nif number > 0:\n    print('موجب')", "explanation": "تُظهر المسافة البادئة أن أمر الطباعة تابع لكتلة if. نضيف أربع مسافات قبل print."},
    {"title": "التحدي الرابع: مقارنة أم إسناد؟", "description": "نريد التحقق من أن الإجابة تساوي 42.", "code": "answer = 42\nif answer = 42:\n    print('صحيح!')", "diagnosis": "يجب استخدام == للمقارنة بدلاً من =", "diagnoses": ["يجب استخدام == للمقارنة بدلاً من =", "يجب حذف العدد 42", "ينقص أمر print فاصلة", "يجب استبدال if بـ for"], "starter": "answer = 42\nif answer = 42:\n    print('صحيح!')", "required": "if answer == 42:", "solution": "answer = 42\nif answer == 42:\n    print('صحيح!')", "explanation": "نستخدم == لمقارنة قيمتين داخل الشرط. أما = فتُستخدم لإسناد قيمة إلى متغيّر."},
]


def initialize_state():
    defaults = {
        "page": "الرئيسية",
        "quiz_index": {level: 0 for level in QUIZ_LEVELS},
        "quiz_attempt": {level: 0 for level in QUIZ_LEVELS},
        "quiz_answers": {},
        "earned_quiz": set(),
        "challenge_results": {},
        "earned_challenges": set(),
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def navigate(page):
    st.session_state.page = page


def total_points():
    return len(st.session_state.earned_quiz) * 10 + len(st.session_state.earned_challenges) * 20


def normalize_code(code):
    """Normalize whitespace for checking the small, known challenge corrections."""
    return "".join(code.split())


initialize_state()

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&display=swap');
    :root { --purple:#a78bfa; --blue:#60a5fa; --text:#f3f0ff; --muted:#b7b2c9; --border:rgba(180,160,255,.18); }
    html, body, [class*="css"], [data-testid="stAppViewContainer"] { font-family:'Cairo',sans-serif; }
    .stApp { color:var(--text); background:radial-gradient(ellipse at 85% 4%,rgba(92,48,170,.24),transparent 34%),radial-gradient(ellipse at 10% 45%,rgba(35,91,174,.16),transparent 35%),#100d19; }
    [data-testid="stHeader"] { background:rgba(16,13,25,.75); }
    [data-testid="stSidebar"] { background:linear-gradient(180deg,#1a1428 0%,#11101c 100%); border-left:1px solid var(--border); }
    [data-testid="stSidebar"] * { text-align:right; }
    .block-container { max-width:1180px; padding-top:2rem; padding-bottom:3rem; direction:rtl; }
    h1,h2,h3,p,label,.stMarkdown { text-align:right; }
    .hero { padding:3rem; margin:.5rem 0 1.5rem; border:1px solid rgba(198,173,255,.26); border-radius:28px; background:radial-gradient(circle at 12% 18%,rgba(96,165,250,.27),transparent 34%),linear-gradient(125deg,rgba(91,45,154,.82),rgba(38,48,106,.78)); box-shadow:0 24px 70px rgba(0,0,0,.28); animation:rise .7s ease-out both; }
    .hero h1 { font-size:clamp(2rem,5vw,3.5rem); margin:.4rem 0; color:#fff; line-height:1.4; }
    .hero p { color:#e4dcff; font-size:1.13rem; margin-bottom:0; }
    .eyebrow { color:#d7c6ff; font-weight:700; }
    .welcome-note { display:flex; align-items:center; gap:.65rem; margin:0 0 1.5rem; padding:1rem 1.25rem; border:1px solid rgba(207,183,255,.32); border-radius:17px; background:linear-gradient(110deg,rgba(124,58,237,.25),rgba(66,107,215,.20)); box-shadow:0 10px 30px rgba(42,27,83,.20); color:#fff; font-size:clamp(1.05rem,2.4vw,1.3rem); font-weight:700; animation:rise .8s ease-out both; }
    .welcome-note span { font-size:1.35em; }
    .section-title { margin:1.8rem 0 1rem; font-weight:800; }
    .card { height:100%; padding:1.25rem 1.35rem; border-radius:20px; border:1px solid var(--border); background:linear-gradient(145deg,rgba(37,31,57,.95),rgba(24,23,40,.9)); box-shadow:0 12px 32px rgba(0,0,0,.18); transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease; text-align:right; }
    .card:hover { transform:translateY(-4px); border-color:rgba(167,139,250,.48); box-shadow:0 18px 38px rgba(58,37,104,.28); }
    .card h3 { margin:.15rem 0 .45rem; color:#fff; font-size:1.13rem; }
    .card p,.small-note { color:var(--muted); line-height:1.8; }
    .card-icon { font-size:1.7rem; margin-bottom:.35rem; }
    .quote-card { padding:2.2rem; border-radius:24px; border:1px solid rgba(207,183,255,.27); background:linear-gradient(135deg,rgba(100,54,158,.36),rgba(41,63,130,.32)); box-shadow:0 18px 55px rgba(0,0,0,.22); }
    .quote-card blockquote { margin:0; color:#fff; font-size:clamp(1.3rem,3vw,2rem); font-weight:700; line-height:2; }
    .badge { padding:1rem; margin:.2rem 0 .6rem; border-radius:16px; border:1px solid var(--border); background:rgba(36,31,54,.82); text-align:right; }
    .badge.locked { opacity:.48; filter:grayscale(.8); }
    .badge strong { color:#fff; }
    .stButton>button { border:1px solid rgba(196,173,255,.3); border-radius:13px; color:white; background:linear-gradient(115deg,#7c3aed,#426bd7); font-weight:700; min-height:2.8rem; transition:transform .18s ease,filter .18s ease; }
    .stButton>button:hover { color:#fff; filter:brightness(1.13); transform:translateY(-2px); border-color:rgba(220,207,255,.6); }
    .stRadio label,.stSelectbox label,.stTextArea label { color:var(--text)!important; }
    [data-testid="stMetric"] { background:rgba(34,29,51,.8); border:1px solid var(--border); padding:1rem; border-radius:16px; }
    [data-testid="stMetricLabel"],[data-testid="stMetricValue"] { text-align:right; }
    code,pre,[data-testid="stCode"] { direction:ltr!important; text-align:left!important; border-radius:12px!important; }
    hr { border-color:rgba(180,160,255,.14); }
    @keyframes rise { from{opacity:0;transform:translateY(14px)} to{opacity:1;transform:translateY(0)} }
    @media(max-width:700px) { .block-container{padding:1rem 1rem 2rem}.hero{padding:2rem 1.35rem;border-radius:21px}.quote-card{padding:1.5rem} }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## 💜 Hiba's Code Arena")
    st.caption("مساحة للتعلّم والتحدّي والإبداع")
    st.markdown("---")
    st.radio("التنقّل", PAGES, key="page", label_visibility="collapsed")
    st.markdown("---")
    st.metric("⭐ مجموع النقاط", total_points())
    st.caption("نقاطك محفوظة خلال جلسة التصفح الحالية.")

page = st.session_state.page

if page == "الرئيسية":
    st.markdown("""
    <section class="hero"><div class="eyebrow">✨ تعلّمي، جرّبي، واصنعي شيئاً رائعاً</div>
    <h1>أهلاً بك في Hiba's Code Arena</h1><p>اكتشف عالم البرمجة وتحدَّ قدراتك!</p></section>
    <div class="welcome-note" dir="rtl"><span>💌</span> هذه رسالة من تلميذك هادي إلى مس هبة ❤️</div>
    """, unsafe_allow_html=True)
    c1, c2, _ = st.columns([1.2, 1.2, 2])
    c1.button("🚀 ابدأ التعلّم", use_container_width=True, on_click=navigate, args=("اختبار بايثون",))
    c2.button("🧠 خُض الاختبار", use_container_width=True, on_click=navigate, args=("اختبار بايثون",))
    st.markdown('<h2 class="section-title">مساحتك للتعلّم</h2>', unsafe_allow_html=True)
    cards = [("🐍", "اختبار بايثون", "15 سؤالاً موزّعة على ثلاثة مستويات، مع شرح فوري للإجابات."), ("🛠️", "تحديات تصحيح الأخطاء", "أربعة تحديات عملية لتكتشفي الأخطاء وتكتبي التصحيح بنفسك."), ("🏆", "النقاط والإنجازات", "اجمعي النقاط، تابعي تقدّمك، وافتحي شارات الإنجاز.")]
    columns = st.columns(3)
    for column, (icon, title, description) in zip(columns, cards):
        with column:
            st.markdown(f'<div class="card"><div class="card-icon">{icon}</div><h3>{title}</h3><p>{description}</p></div>', unsafe_allow_html=True)
    completed = len(st.session_state.earned_quiz) + len(st.session_state.earned_challenges)
    st.markdown('<h2 class="section-title">رحلتك حتى الآن</h2>', unsafe_allow_html=True)
    st.progress(completed / 19)
    st.caption(f"أنجزتِ {len(st.session_state.earned_quiz)} إجابات صحيحة و{len(st.session_state.earned_challenges)} تحديات.")

elif page == "اختبار بايثون":
    st.title("🧠 اختبار بايثون")
    st.markdown('<p class="small-note">اختاري مستواك، أجيبي عن الأسئلة، وتعرّفي على سبب صحة كل إجابة.</p>', unsafe_allow_html=True)
    level = st.selectbox("المستوى", list(QUIZ_LEVELS), key="selected_level")
    questions = QUIZ_LEVELS[level]
    index = st.session_state.quiz_index[level]
    attempt = st.session_state.quiz_attempt[level]
    level_correct = sum(f"{level}:{i}" in st.session_state.earned_quiz for i in range(len(questions)))
    a, b = st.columns(2)
    a.info(f"المستوى: **{level}** · {len(questions)} أسئلة")
    b.info(f"إجابات صحيحة: **{level_correct} / {len(questions)}**")
    if index >= len(questions):
        st.success(f"أكملتِ مستوى {level}! أحسنتِ 🌟")
        st.write(f"الإجابات الصحيحة التي حققتِها: **{level_correct} من {len(questions)}**.")
        if st.button("🔁 إعادة المستوى", key=f"restart_{level}"):
            st.session_state.quiz_index[level] = 0
            st.session_state.quiz_attempt[level] += 1
            st.rerun()
    else:
        item = questions[index]
        answer_key = f"{level}:{attempt}:{index}"
        st.progress(index / len(questions))
        st.markdown(f"### السؤال {index + 1} من {len(questions)}")
        st.markdown(f"#### {item['question']}")
        selected = st.radio("اختاري إجابة واحدة:", item["options"], key=f"answer_{level}_{attempt}_{index}", label_visibility="collapsed")
        if answer_key in st.session_state.quiz_answers:
            chosen = st.session_state.quiz_answers[answer_key]
            if chosen == item["answer"]:
                st.success(f"إجابة صحيحة! 🎉 {item['explanation']}")
            else:
                st.error(f"ليست الإجابة الصحيحة هذه المرة. الإجابة الصحيحة هي: **{item['answer']}**")
                st.info(item["explanation"])
            if st.button("السؤال التالي ←", key=f"next_{level}_{attempt}_{index}"):
                st.session_state.quiz_index[level] += 1
                st.rerun()
        elif st.button("تحقّقي من الإجابة", key=f"submit_{level}_{attempt}_{index}"):
            st.session_state.quiz_answers[answer_key] = selected
            if selected == item["answer"]:
                st.session_state.earned_quiz.add(f"{level}:{index}")
                st.toast("أُضيفت 10 نقاط إلى رصيدك! ⭐")
            st.rerun()
        st.caption("تحصلين على 10 نقاط عند الإجابة الصحيحة، مرة واحدة لكل سؤال.")

elif page == "تحديات تصحيح الأخطاء":
    st.title("🛠️ تحديات تصحيح الأخطاء")
    st.markdown('<p class="small-note">اقرئي الكود، حدّدي نوع الخطأ، ثم عدّلي الكود في المحرّر واضغطي على زر التحقّق.</p>', unsafe_allow_html=True)
    for i, challenge in enumerate(CHALLENGES):
        with st.container(border=True):
            st.markdown(f"### {challenge['title']}")
            st.write(challenge["description"])
            st.code(challenge["code"], language="python")
            diagnosis = st.radio("ما الخطأ الذي تلاحظينه؟", challenge["diagnoses"], key=f"diagnosis_{i}")
            edited_code = st.text_area("اكتبي النسخة المصححة من الكود:", value=challenge["starter"], height=120, key=f"edited_code_{i}")
            if st.button("تحقّقي من الحل", key=f"check_challenge_{i}"):
                diagnosis_correct = diagnosis == challenge["diagnosis"]
                code_correct = normalize_code(challenge["required"]) in normalize_code(edited_code)
                st.session_state.challenge_results[i] = {"diagnosis_correct": diagnosis_correct, "code_correct": code_correct}
                if diagnosis_correct and code_correct:
                    st.session_state.earned_challenges.add(i)
                st.rerun()
            result = st.session_state.challenge_results.get(i)
            if result:
                if result["diagnosis_correct"] and result["code_correct"]:
                    st.success("ممتاز! حدّدتِ الخطأ وأصلحتِ الكود بشكل صحيح. 🌟")
                else:
                    if not result["diagnosis_correct"]:
                        st.warning(f"راجعي تشخيص الخطأ. تلميح: {challenge['explanation']}")
                    if not result["code_correct"]:
                        st.warning("الكود لا يزال يحتاج إلى تعديل. قارني التعديل المطلوب بالحل أدناه.")
            with st.expander("عرض الحل والتفسير"):
                st.code(challenge["solution"], language="python")
                st.write(challenge["explanation"])
    st.caption("تُمنح 20 نقطة لكل تحدٍ عند تحديد الخطأ وكتابة التصحيح الصحيح.")

elif page == "إنجازاتي":
    st.title("🏆 إنجازاتي")
    st.markdown('<p class="small-note">كل إجابة صحيحة وتحدٍ مكتمل يقرّبانك من إنجاز جديد.</p>', unsafe_allow_html=True)
    points = total_points()
    quiz_count = len(st.session_state.earned_quiz)
    challenge_count = len(st.session_state.earned_challenges)
    completed = quiz_count + challenge_count
    c1, c2, c3 = st.columns(3)
    c1.metric("⭐ مجموع النقاط", points)
    c2.metric("✅ أسئلة صحيحة", f"{quiz_count} / 15")
    c3.metric("🛠️ تحديات مكتملة", f"{challenge_count} / 4")
    st.markdown("### تقدّم التعلّم")
    st.progress(completed / 19)
    st.caption(f"أنجزتِ {completed} من 19 فرصة تعلّم.")
    badges = [("🌱", "بداية جميلة", "اجمعي 10 نقاط.", points >= 10), ("✨", "نجمة ساطعة", "اجمعي 50 نقطة.", points >= 50), ("💎", "مبدعة البرمجة", "اجمعي 100 نقطة.", points >= 100), ("🧠", "خبيرة الاختبار", "أجيبي إجابة صحيحة عن الأسئلة الخمسة عشر.", quiz_count == 15), ("🛠️", "صائدة الأخطاء", "أكملي تحديات تصحيح الأخطاء الأربعة.", challenge_count == 4), ("🏆", "بطلة الساحة", "أكملي كل أسئلة الاختبار والتحديات.", completed == 19)]
    st.markdown("### شاراتك")
    cols = st.columns(2)
    for i, (icon, title, description, unlocked) in enumerate(badges):
        with cols[i % 2]:
            state = "" if unlocked else "locked"
            status = "مفتوحة" if unlocked else "مقفلة"
            st.markdown(f'<div class="badge {state}"><strong>{icon} {title} · {status}</strong><br><span class="small-note">{description}</span></div>', unsafe_allow_html=True)
    st.caption("تُحفظ النقاط والإنجازات في جلسة المتصفح الحالية.")

elif page == "إلى المعلمة هبة":
    st.title("💜 رسالة خاصة")
    st.markdown("""<div class="quote-card"><div class="eyebrow">بكل المحبة والامتنان</div>
    <blockquote>إلى المعلمة هبة، شكراً لأنك جعلتِ البرمجة عالماً ممتعاً ومميزاً.</blockquote>
    <p class="small-note">هذا المشروع إهداء تقديرٍ لكل معلمة تلهم طالباتها.</p></div>""", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("<div class='card'><h3>🌷 شكراً لكِ يا معلمتي</h3><p>بفضل شغفكِ وصبركِ، أصبحت كتابة الكود رحلة مليئة بالاكتشاف. نتمنى أن تكون هذه الساحة الصغيرة تذكيراً جميلاً بالأثر الكبير الذي تصنعه المعلمة.</p></div>", unsafe_allow_html=True)

elif page == "عن المشروع":
    st.title("ℹ️ عن المشروع")
    st.markdown('<p class="small-note">تعرّفي على فكرة Hiba\'s Code Arena والتقنيات التي بُنيت بها.</p>', unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>🎯 فكرة المشروع</h3><p>Hiba's Code Arena مشروع تعليمي تفاعلي يهدف إلى جعل تعلّم أساسيات البرمجة ممتعاً. يجمع بين اختبار بايثون بمستويات مختلفة وتحديات عملية لتصحيح أخطاء الكود، مع نقاط وشارات تساعد على متابعة التقدّم.</p></div>", unsafe_allow_html=True)
    st.markdown("")
    left, right = st.columns(2)
    with left:
        st.markdown("<div class='card'><h3>🐍 Python</h3><p>لغة البرمجة المستخدمة في بناء التطبيق والمحتوى التعليمي.</p></div>", unsafe_allow_html=True)
    with right:
        st.markdown("<div class='card'><h3>⚡ Streamlit</h3><p>إطار عمل يسهّل إنشاء تطبيقات ويب تفاعلية باستخدام Python.</p></div>", unsafe_allow_html=True)
    st.markdown("")
    st.info("هذا المشروع نشاط تعليمي للتعريف بالبرمجة وتصميم تطبيق ويب تفاعلي.")
    st.markdown("**المحتوى:** 15 سؤالاً · 3 مستويات · 4 تحديات تصحيح أخطاء · نظام نقاط وشارات")
