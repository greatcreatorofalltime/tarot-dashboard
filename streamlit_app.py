import streamlit as st
import random
import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Daily Tarot Oracle",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Language texts dictionary
texts = {
    "en": {
        "app_title": "DAILY TAROT ORACLE",
        "app_subtitle": "Daily Guidance • Ancient Wisdom • Trust Your Intuition",
        "sidebar_title": "Sacred Space",
        "preparation": "Preparation",
        "preparation_text": "Center yourself, breathe deeply, and focus your intention on your question.",
        "spread_meanings": "Spread Meanings",
        "spread_single": "Single Card: Daily guidance",
        "spread_three": "Three Cards: Past, Present, Future",
        "spread_celtic": "Celtic Cross: Deep life insight",
        "visit_shop": "Visit Our Shop",
        "shop_text": "Explore spiritual journals, tarot guides, and mystical tools in our store.",
        "enter_shop": "Enter the Journaling Universe",
        "deck_info": "Complete 78-Card Deck",
        "deck_text": "This reading uses the full traditional tarot deck including:",
        "deck_major": "22 Major Arcana",
        "deck_minor": "56 Minor Arcana",
        "deck_suits": "All four suits: Wands, Cups, Swords, Pentacles",
        "trust_intuition": "Trust your intuition above all else. The cards are mirrors, not masters.",
        "sacred_question": "Your Sacred Question",
        "question_placeholder": "Whisper your question to the universe...\n\nWhat guidance do I need today?\nWhat path should I follow?\nWhat is hidden that I need to see?",
        "choose_spread": "Choose Your Spread",
        "consult_oracle": "CONSULT THE ORACLE",
        "focus_intention": "Please focus your intention with a question",
        "cards_spoken": "The Cards Have Spoken",
        "reading_cast": "Reading cast on",
        "sacred_spread": "The Sacred Spread",
        "sacred_interpretations": "Sacred Interpretations",
        "position": "Position",
        "meaning": "Meaning",
        "guidance": "Guidance",
        "suit": "Suit",
        "element": "Element",
        "cosmic_guidance": "Cosmic Guidance",
        "truths": "Remember These Truths",
        "truth_text": '"The cards reflect possibilities, not certainties. Your free will shapes your destiny. Take what resonates, release what does not, and always trust your inner wisdom above all else."',
        "save_reading": "Save This Reading to Your Book of Shadows",
        "download_record": "Download Sacred Record",
        "cards_await": "The Cards Await Your Question",
        "instructions": "Enter your sacred question in the space provided, choose your spread, and click 'Consult the Oracle' to receive divine guidance.",
        "trust_process": "Trust the process",
        "listen_intuition": "Listen to your intuition",
        "embrace_wisdom": "Embrace the wisdom that comes",
        "continue_journey": "Continue Your Spiritual Journey",
        "shop_promo": "Explore our collection of spiritual journals and tools to deepen your practice",
        "footer_text": "Daily Tarot Oracle • Complete 78-Card Traditional Deck • Ancient Wisdom for Modern Times",
        "visit_shop_footer": "Visit Our Shop: Journaling The Universe",
        "disclaimer": "This reading is for spiritual guidance and self-reflection only. Always trust your own judgment in making life decisions.",
        # Spread options for dropdown
        "spread_single_option": "Single Card • Daily Guidance",
        "spread_three_option": "Three Cards • Past, Present, Future", 
        "spread_celtic_option": "Celtic Cross • Comprehensive Insight"
    },
    "zh": {
        "app_title": "每日塔羅神諭",
        "app_subtitle": "每日指引 • 古老智慧 • 信任你的直覺",
        "sidebar_title": "神聖對話",
        "preparation": "準備工作",
        "preparation_text": "靜心凝神，深呼吸，將意圖專注於你的問題上。",
        "spread_meanings": "牌陣意義",
        "spread_single": "單張牌：每日指引",
        "spread_three": "三張牌：過去、現在、未來",
        "spread_celtic": "凱爾特十字：深度人生洞察",
        "visit_shop": "訪問我們的商店",
        "shop_text": "探索我們商店中的靈性日記、塔羅指南和神秘工具。",
        "enter_shop": "進入宇宙日記",
        "deck_info": "完整78張牌組",
        "deck_text": "本次占卜使用完整的傳統塔羅牌組，包括：",
        "deck_major": "22張大阿卡納",
        "deck_minor": "56張小阿卡納",
        "deck_suits": "全部四組花色：權杖、聖杯、寶劍、錢幣",
        "trust_intuition": "最重要的是信任你的直覺。塔羅牌是鏡子，不是主人。",
        "sacred_question": "你的神聖問題",
        "question_placeholder": "向宇宙輕聲訴說你的問題...\n\n我今天需要什麼指引？\n我應該走什麼道路？\n有什麼隱藏的事物我需要看見？",
        "choose_spread": "選擇你的牌陣",
        "consult_oracle": "請教神諭",
        "focus_intention": "請專注你的意圖，提出一個問題",
        "cards_spoken": "塔羅牌已經發言",
        "reading_cast": "占卜時間",
        "sacred_spread": "神聖牌陣",
        "sacred_interpretations": "神聖解讀",
        "position": "位置",
        "meaning": "意義",
        "guidance": "指引",
        "suit": "花色",
        "element": "元素",
        "cosmic_guidance": "宇宙指引",
        "truths": "記住這些真理",
        "truth_text": '"塔羅牌反映可能性，而非確定性。你的自由意志塑造你的命運。接受引起共鳴的，放下不適合的，永遠信任你內在的智慧。"',
        "save_reading": "將此占卜保存到你的影子之書",
        "download_record": "下載神聖記錄",
        "cards_await": "塔羅牌等待你的問題",
        "instructions": "在提供的空間輸入你的神聖問題，選擇牌陣，然後點擊'請教神諭'接收神聖指引。",
        "trust_process": "信任過程",
        "listen_intuition": "聆聽直覺",
        "embrace_wisdom": "擁抱到來的智慧",
        "continue_journey": "繼續你的靈性旅程",
        "shop_promo": "探索我們的靈性日記和工具收藏，深化你的修行",
        "footer_text": "每日塔羅神諭 • 完整78張傳統牌組 • 現代時代的古老智慧",
        "visit_shop_footer": "訪問我們的商店：宇宙日記",
        "disclaimer": "此占卜僅供靈性指引和自我反思使用。在做出人生決定時，請始終信任你自己的判斷。",
        # Spread options for dropdown - fixed separate entries
        "spread_single_option": "單張牌 • 每日指引",
        "spread_three_option": "三張牌 • 過去、現在、未來", 
        "spread_celtic_option": "凱爾特十字 • 深度人生洞察"
    }
}

# Fixed CSS with proper background handling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=MedievalSharp&family=Noto+Sans+SC:wght@400;500;700&display=swap');
    
    .main-header {
        font-family: 'Cinzel', 'Noto Sans SC', serif;
        font-size: 3.5rem;
        background: linear-gradient(45deg, #D4AF37, #FFD700, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 0 0 30px rgba(212, 175, 55, 0.3);
        padding-top: 1rem;
    }
    .subtitle {
        font-family: 'Cinzel', 'Noto Sans SC', serif;
        text-align: center;
        color: #b8b8b8;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        letter-spacing: 2px;
    }
    .tarot-card {
        background: linear-gradient(145deg, #1e1e2e, #2d2d44);
        border: 2px solid #D4AF37;
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
    }
    .tarot-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(212, 175, 55, 0.2);
    }
    .card-image {
        font-size: 4rem;
        margin-bottom: 15px;
        filter: drop-shadow(0 0 10px rgba(212, 175, 55, 0.5));
    }
    .card-name {
        font-family: 'Cinzel', 'Noto Sans SC', serif;
        color: #D4AF37;
        font-size: 1.2rem;
        font-weight: 600;
        margin: 10px 0;
    }
    .interpretation-box {
        background: rgba(30, 30, 46, 0.8);
        border: 1px solid #444;
        border-radius: 12px;
        padding: 25px;
        margin: 15px 0;
        backdrop-filter: blur(10px);
        border-left: 4px solid #D4AF37;
    }
    .question-box {
        background: rgba(30, 30, 46, 0.6);
        border: 1px solid #444;
        border-radius: 12px;
        padding: 25px;
        margin: 20px 0;
        border-top: 2px solid #D4AF37;
    }
    .gold-text {
        color: #D4AF37;
        font-family: 'Cinzel', 'Noto Sans SC', serif;
    }
    .silver-text {
        color: #b8b8b8;
    }
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #D4AF37, transparent);
        margin: 30px 0;
    }
    .spread-title {
        font-family: 'Cinzel', 'Noto Sans SC', serif;
        text-align: center;
        color: #D4AF37;
        margin: 25px 0;
        font-size: 1.8rem;
    }
    .stButton button {
        background: linear-gradient(45deg, #D4AF37, #FFD700);
        color: #1a1a2e;
        border: none;
        padding: 12px 30px;
        border-radius: 25px;
        font-family: 'Cinzel', 'Noto Sans SC', serif;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
        background: linear-gradient(45deg, #FFD700, #D4AF37);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    .reversed {
        color: #ff6b6b;
        font-style: italic;
    }
    .upright {
        color: #51cf66;
        font-style: italic;
    }
    
    /* Main background styling */
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
        color: #e6e6e6;
    }
    
    /* Fix the main content area */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Ensure proper spacing */
    .css-1d391kg {
        padding-top: 0rem;
    }
    
    /* Custom link styling */
    .store-link {
        display: inline-block;
        background: linear-gradient(45deg, #D4AF37, #FFD700);
        color: #1a1a2e !important;
        padding: 10px 20px;
        border-radius: 20px;
        text-decoration: none;
        font-family: 'Cinzel', 'Noto Sans SC', serif;
        font-weight: 600;
        margin: 10px 0;
        transition: all 0.3s ease;
        text-align: center;
    }
    .store-link:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
        background: linear-gradient(45deg, #FFD700, #D4AF37);
        color: #1a1a2e;
        text-decoration: none;
    }
    
    /* Shop promotion styling that blends with theme */
    .shop-promotion {
        background: rgba(30, 30, 46, 0.7) !important;
        border: 1px solid #444 !important;
        border-radius: 12px;
        padding: 25px;
        margin: 20px 0;
        backdrop-filter: blur(10px);
        border-left: 4px solid #D4AF37 !important;
    }
    
    /* Language selector styling */
    .language-selector {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 1000;
    }
</style>
""", unsafe_allow_html=True)

# Complete 78 Tarot Cards Database with Chinese translations
tarot_cards = {
    # MAJOR ARCANA (22 cards)
    "The Fool": {"name_zh": "愚者", "meaning": "New beginnings, innocence, spontaneity, free spirit.", "meaning_zh": "新的開始、天真、自發性、自由精神。", "reversed": "Recklessness, risk-taking, poor judgment.", "reversed_zh": "魯莽、冒險、判斷力差。", "advice": "Embrace new opportunities with an open heart.", "advice_zh": "以開放的心態擁抱新機會。", "image": "🎭", "element": "Air", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Magician": {"name_zh": "魔法師", "meaning": "Manifestation, power, resourcefulness, skill.", "meaning_zh": "顯化、力量、機智、技能。", "reversed": "Manipulation, untapped talents, trickery.", "reversed_zh": "操縱、未開發的才能、欺騙。", "advice": "Use your skills and resources to manifest your desires.", "advice_zh": "運用你的技能和資源來顯化你的願望。", "image": "🎩", "element": "Mercury", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The High Priestess": {"name_zh": "女祭司", "meaning": "Intuition, mystery, subconscious mind, divine feminine.", "meaning_zh": "直覺、神秘、潛意識、神聖女性。", "reversed": "Secrets, hidden agendas, withdrawal.", "reversed_zh": "秘密、隱藏議程、退縮。", "advice": "Trust your intuition and inner wisdom.", "advice_zh": "信任你的直覺和內在智慧。", "image": "🌙", "element": "Water", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Empress": {"name_zh": "皇后", "meaning": "Femininity, beauty, nature, abundance, nurturing.", "meaning_zh": "女性特質、美麗、自然、豐盛、滋養。", "reversed": "Creative block, dependence on others, neglect.", "reversed_zh": "創造力阻塞、依賴他人、忽視。", "advice": "Nurture your creativity and connect with nature.", "advice_zh": "培養創造力並與自然連結。", "image": "👑", "element": "Venus", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Emperor": {"name_zh": "皇帝", "meaning": "Authority, structure, control, fatherhood.", "meaning_zh": "權威、結構、控制、父性。", "reversed": "Domination, rigidity, lack of discipline.", "reversed_zh": "支配、僵化、缺乏紀律。", "advice": "Establish structure and take authority in your life.", "advice_zh": "在生活中建立結構並行使權威。", "image": "⚜️", "element": "Fire", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Hierophant": {"name_zh": "教皇", "meaning": "Tradition, spirituality, education, conformity.", "meaning_zh": "傳統、靈性、教育、順從。", "reversed": "Rebellion, unconventional beliefs, restriction.", "reversed_zh": "叛逆、非傳統信仰、限制。", "advice": "Seek spiritual guidance and honor traditions.", "advice_zh": "尋求靈性指導並尊重傳統。", "image": "📜", "element": "Earth", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Lovers": {"name_zh": "戀人", "meaning": "Love, harmony, relationships, choices.", "meaning_zh": "愛情、和諧、關係、選擇。", "reversed": "Disharmony, imbalance, misalignment of values.", "reversed_zh": "不和諧、不平衡、價值觀不一致。", "advice": "Choose love and alignment with your true values.", "advice_zh": "選擇愛與你真正價值觀的一致性。", "image": "💞", "element": "Air", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Chariot": {"name_zh": "戰車", "meaning": "Willpower, determination, success, control.", "meaning_zh": "意志力、決心、成功、控制。", "reversed": "Lack of direction, aggression, no control.", "reversed_zh": "缺乏方向、侵略性、無法控制。", "advice": "Use your willpower to overcome obstacles.", "advice_zh": "運用意志力克服障礙。", "image": "🏆", "element": "Water", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "Strength": {"name_zh": "力量", "meaning": "Courage, persuasion, influence, compassion.", "meaning_zh": "勇氣、說服力、影響力、同情心。", "reversed": "Inner weakness, insecurity, lack of self-control.", "reversed_zh": "內在軟弱、不安全感、缺乏自制力。", "advice": "Have courage and compassion.", "advice_zh": "擁有勇氣和同情心。", "image": "🦁", "element": "Fire", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Hermit": {"name_zh": "隱士", "meaning": "Soul-searching, introspection, guidance, solitude.", "meaning_zh": "靈魂探索、內省、指導、獨處。", "reversed": "Isolation, loneliness, withdrawal.", "reversed_zh": "孤立、孤獨、退縮。", "advice": "Take time for introspection.", "advice_zh": "花時間進行內省。", "image": "🕯️", "element": "Earth", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "Wheel of Fortune": {"name_zh": "命運之輪", "meaning": "Cycles, fate, turning points, destiny.", "meaning_zh": "循環、命運、轉折點、宿命。", "reversed": "Bad luck, resistance to change, unwelcome disruption.", "reversed_zh": "厄運、抗拒改變、不受歡迎的干擾。", "advice": "Accept the natural cycles of life.", "advice_zh": "接受生命的自然循環。", "image": "🔄", "element": "Fire", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "Justice": {"name_zh": "正義", "meaning": "Fairness, truth, cause and effect, law.", "meaning_zh": "公平、真理、因果、法律。", "reversed": "Injustice, dishonesty, unfairness, lack of accountability.", "reversed_zh": "不公正、不誠實、不公平、缺乏責任感。", "advice": "Seek truth and fairness.", "advice_zh": "尋求真理和公平。", "image": "⚖️", "element": "Air", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Hanged Man": {"name_zh": "倒吊人", "meaning": "Surrender, new perspective, enlightenment, suspension.", "meaning_zh": "投降、新視角、啟蒙、懸掛。", "reversed": "Stalling, resistance, martyrdom, indecision.", "reversed_zh": "拖延、抵抗、殉道、猶豫不決。", "advice": "Let go and gain a new perspective.", "advice_zh": "放手並獲得新視角。", "image": "🙃", "element": "Water", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "Death": {"name_zh": "死神", "meaning": "Endings, transformation, transition, new beginnings.", "meaning_zh": "結束、轉化、過渡、新的開始。", "reversed": "Resistance to change, stagnation, fear of endings.", "reversed_zh": "抗拒改變、停滯、害怕結束。", "advice": "Embrace necessary endings.", "advice_zh": "擁抱必要的結束。", "image": "💀", "element": "Water", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "Temperance": {"name_zh": "節制", "meaning": "Balance, moderation, patience, purpose.", "meaning_zh": "平衡、節制、耐心、目的。", "reversed": "Imbalance, excess, conflict, hastiness.", "reversed_zh": "不平衡、過度、衝突、倉促。", "advice": "Practice moderation and patience.", "advice_zh": "實踐節制和耐心。", "image": "⚗️", "element": "Fire", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Devil": {"name_zh": "惡魔", "meaning": "Bondage, addiction, materialism, shadow self.", "meaning_zh": "束縛、成癮、物質主義、陰影自我。", "reversed": "Release, independence, reclaiming power.", "reversed_zh": "釋放、獨立、重新獲得力量。", "advice": "Confront your attachments and limitations.", "advice_zh": "面對你的執著和限制。", "image": "😈", "element": "Earth", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Tower": {"name_zh": "高塔", "meaning": "Sudden change, upheaval, revelation, awakening.", "meaning_zh": "突然改變、動盪、啟示、覺醒。", "reversed": "Fear of change, avoiding disaster, delaying the inevitable.", "reversed_zh": "害怕改變、避免災難、延遲不可避免的事。", "advice": "Embrace necessary destruction.", "advice_zh": "擁抱必要的摧毀。", "image": "🏰", "element": "Fire", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Star": {"name_zh": "星星", "meaning": "Hope, inspiration, serenity, faith.", "meaning_zh": "希望、靈感、寧靜、信念。", "reversed": "Hopelessness, despair, lack of faith.", "reversed_zh": "絕望、沮喪、缺乏信念。", "advice": "Have faith and hope.", "advice_zh": "擁有信念和希望。", "image": "⭐", "element": "Air", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Moon": {"name_zh": "月亮", "meaning": "Illusion, intuition, subconscious, dreams.", "meaning_zh": "幻覺、直覺、潛意識、夢境。", "reversed": "Confusion, fear, misinterpretation.", "reversed_zh": "困惑、恐懼、誤解。", "advice": "Trust your intuition through uncertain times.", "advice_zh": "在不確定的時期信任你的直覺。", "image": "🌕", "element": "Water", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The Sun": {"name_zh": "太陽", "meaning": "Joy, success, celebration, positivity.", "meaning_zh": "喜悅、成功、慶祝、積極。", "reversed": "Temporary sadness, lack of success, inflated ego.", "reversed_zh": "暫時的悲傷、缺乏成功、膨脹的自我。", "advice": "Embrace joy and success.", "advice_zh": "擁抱喜悅和成功。", "image": "☀️", "element": "Fire", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "Judgement": {"name_zh": "審判", "meaning": "Rebirth, inner calling, absolution, awakening.", "meaning_zh": "重生、內在召喚、赦免、覺醒。", "reversed": "Self-doubt, refusal of call, fear of judgment.", "reversed_zh": "自我懷疑、拒絕召喚、害怕評判。", "advice": "Answer your inner calling.", "advice_zh": "回應你的內在召喚。", "image": "👼", "element": "Water", "suit": "Major Arcana", "suit_zh": "大阿卡納"},
    "The World": {"name_zh": "世界", "meaning": "Completion, achievement, travel, fulfillment.", "meaning_zh": "完成、成就、旅行、實現。", "reversed": "Incompletion, lack of closure, delays.", "reversed_zh": "未完成、缺乏結束、延遲。", "advice": "Celebrate your achievements and prepare for new cycles.", "advice_zh": "慶祝你的成就並為新循環做準備。", "image": "🌍", "element": "Earth", "suit": "Major Arcana", "suit_zh": "大阿卡納"},

    # WANDS SUIT (14 cards)
    "Ace of Wands": {"name_zh": "權杖王牌", "meaning": "Inspiration, new opportunities, growth, potential.", "meaning_zh": "靈感、新機會、成長、潛力。", "reversed": "Delays, lack of motivation, missed opportunities.", "reversed_zh": "延遲、缺乏動力、錯失機會。", "advice": "Pursue new passions and creative endeavors.", "advice_zh": "追求新的熱情和創造性努力。", "image": "🔥", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Two of Wands": {"name_zh": "權杖二", "meaning": "Planning, discovery, decisions, future planning.", "meaning_zh": "計劃、發現、決定、未來規劃。", "reversed": "Fear of unknown, lack of planning, bad decisions.", "reversed_zh": "害怕未知、缺乏計劃、壞決定。", "advice": "Make bold plans for the future.", "advice_zh": "為未來制定大膽計劃。", "image": "🗺️", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Three of Wands": {"name_zh": "權杖三", "meaning": "Expansion, foresight, overseas opportunities, progress.", "meaning_zh": "擴展、遠見、海外機會、進步。", "reversed": "Obstacles, delays, frustration, limited vision.", "reversed_zh": "障礙、延遲、挫折、有限視野。", "advice": "Expand your horizons.", "advice_zh": "擴展你的視野。", "image": "⛵", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Four of Wands": {"name_zh": "權杖四", "meaning": "Celebration, harmony, marriage, home, community.", "meaning_zh": "慶祝、和諧、婚姻、家庭、社區。", "reversed": "Conflict, transition, lack of support, home issues.", "reversed_zh": "衝突、過渡、缺乏支持、家庭問題。", "advice": "Celebrate your achievements.", "advice_zh": "慶祝你的成就。", "image": "🎉", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Five of Wands": {"name_zh": "權杖五", "meaning": "Conflict, competition, tension, rivalry.", "meaning_zh": "衝突、競爭、緊張、對抗。", "reversed": "Avoiding conflict, tension release, finding common ground.", "reversed_zh": "避免衝突、釋放緊張、找到共同點。", "advice": "Embrace healthy competition.", "advice_zh": "擁抱健康競爭。", "image": "⚔️", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Six of Wands": {"name_zh": "權杖六", "meaning": "Victory, success, public recognition, progress.", "meaning_zh": "勝利、成功、公眾認可、進步。", "reversed": "Failure, lack of recognition, egotism, fall from grace.", "reversed_zh": "失敗、缺乏認可、自我中心、失寵。", "advice": "Celebrate your successes.", "advice_zh": "慶祝你的成功。", "image": "🏅", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Seven of Wands": {"name_zh": "權杖七", "meaning": "Perseverance, defense, maintaining control, challenge.", "meaning_zh": "堅持、防禦、保持控制、挑戰。", "reversed": "Give up, overwhelmed, yielding, burnout.", "reversed_zh": "放棄、不堪重負、屈服、精疲力盡。", "advice": "Defend your position with courage.", "advice_zh": "勇敢地捍衛你的立場。", "image": "🛡️", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Eight of Wands": {"name_zh": "權杖八", "meaning": "Speed, action, movement, quick decisions.", "meaning_zh": "速度、行動、移動、快速決定。", "reversed": "Delays, frustration, waiting, panic.", "reversed_zh": "延遲、挫折、等待、恐慌。", "advice": "Act quickly on opportunities.", "advice_zh": "快速把握機會。", "image": "🏹", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Nine of Wands": {"name_zh": "權杖九", "meaning": "Resilience, courage, persistence, boundaries.", "meaning_zh": "韌性、勇氣、堅持、界限。", "reversed": "Stubbornness, defensiveness, paranoia, giving up.", "reversed_zh": "固執、防禦性、偏執、放棄。", "advice": "Stay resilient and maintain your boundaries.", "advice_zh": "保持韌性並維護你的界限。", "image": "🎯", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Ten of Wands": {"name_zh": "權杖十", "meaning": "Burden, responsibility, hard work, completion.", "meaning_zh": "負擔、責任、努力工作、完成。", "reversed": "Failure to delegate, collapse, release, shedding load.", "reversed_zh": "未能委派、崩潰、釋放、卸下負擔。", "advice": "Delegate tasks and lighten your load.", "advice_zh": "委派任務並減輕你的負擔。", "image": "💼", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Page of Wands": {"name_zh": "權杖侍從", "meaning": "Exploration, excitement, freedom, discovery.", "meaning_zh": "探索、興奮、自由、發現。", "reversed": "Bad news, delays, fear of failure, immaturity.", "reversed_zh": "壞消息、延遲、害怕失敗、不成熟。", "advice": "Embrace new adventures and creative exploration.", "advice_zh": "擁抱新冒險和創造性探索。", "image": "📜", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Knight of Wands": {"name_zh": "權杖騎士", "meaning": "Action, adventure, fearlessness, energy.", "meaning_zh": "行動、冒險、無畏、能量。", "reversed": "Haste, scattered energy, impulsiveness, delays.", "reversed_zh": "匆忙、分散的能量、衝動、延遲。", "advice": "Channel your energy productively.", "advice_zh": "有效引導你的能量。", "image": "🐎", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "Queen of Wands": {"name_zh": "權杖皇后", "meaning": "Courage, confidence, independence, determination.", "meaning_zh": "勇氣、自信、獨立、決心。", "reversed": "Jealousy, insecurity, selfishness, manipulation.", "reversed_zh": "嫉妒、不安全感、自私、操縱。", "advice": "Embrace your personal power and confidence.", "advice_zh": "擁抱你的個人力量和自信。", "image": "👸", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},
    "King of Wands": {"name_zh": "權杖國王", "meaning": "Leadership, vision, entrepreneur, honor.", "meaning_zh": "領導力、願景、企業家、榮譽。", "reversed": "Impulsiveness, haste, ruthless, overpowering.", "reversed_zh": "衝動、匆忙、無情、壓倒性。", "advice": "Lead with vision and integrity.", "advice_zh": "以願景和誠信領導。", "image": "🤴", "element": "Fire", "suit": "Wands", "suit_zh": "權杖"},

    # CUPS SUIT (14 cards)
    "Ace of Cups": {"name_zh": "聖杯王牌", "meaning": "New love, compassion, creativity, intuition.", "meaning_zh": "新愛情、同情心、創造力、直覺。", "reversed": "Emotional loss, blocked creativity, emptiness.", "reversed_zh": "情感損失、阻塞的創造力、空虛。", "advice": "Open your heart to new emotional experiences.", "advice_zh": "向新的情感體驗敞開心扉。", "image": "💧", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Two of Cups": {"name_zh": "聖杯二", "meaning": "Partnership, union, attraction, connection.", "meaning_zh": "夥伴關係、結合、吸引、連結。", "reversed": "Breakup, imbalance, miscommunication, separation.", "reversed_zh": "分手、不平衡、誤解、分離。", "advice": "Nurture your relationships and seek harmony.", "advice_zh": "培養你的關係並尋求和諧。", "image": "💑", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Three of Cups": {"name_zh": "聖杯三", "meaning": "Celebration, friendship, creativity, community.", "meaning_zh": "慶祝、友誼、創造力、社區。", "reversed": "Isolation, gossip, excess, third party.", "reversed_zh": "孤立、閒話、過度、第三方。", "advice": "Celebrate with friends and community.", "advice_zh": "與朋友和社區一起慶祝。", "image": "🎊", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Four of Cups": {"name_zh": "聖杯四", "meaning": "Meditation, contemplation, apathy, reevaluation.", "meaning_zh": "冥想、沉思、冷漠、重新評估。", "reversed": "New opportunities, acceptance, engagement, clarity.", "reversed_zh": "新機會、接受、參與、清晰。", "advice": "Take time for introspection.", "advice_zh": "花時間進行內省。", "image": "🧘", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Five of Cups": {"name_zh": "聖杯五", "meaning": "Loss, grief, disappointment, regret.", "meaning_zh": "損失、悲傷、失望、遺憾。", "reversed": "Acceptance, moving on, finding peace, forgiveness.", "reversed_zh": "接受、繼續前進、找到平靜、寬恕。", "advice": "Acknowledge your grief but don't dwell on it.", "advice_zh": "承認你的悲傷但不要沉溺其中。", "image": "😔", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Six of Cups": {"name_zh": "聖杯六", "meaning": "Familiarity, happy memories, healing, childhood.", "meaning_zh": "熟悉感、快樂回憶、療癒、童年。", "reversed": "Living in past, stagnation, moving forward.", "reversed_zh": "活在過去、停滯、向前邁進。", "advice": "Cherish happy memories but live in the present.", "advice_zh": "珍惜快樂回憶但要活在當下。", "image": "🏡", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Seven of Cups": {"name_zh": "聖杯七", "meaning": "Choices, illusion, fantasy, wishful thinking.", "meaning_zh": "選擇、幻覺、幻想、一廂情願。", "reversed": "Clarity, decision, alignment, focus.", "reversed_zh": "清晰、決定、對齊、專注。", "advice": "Distinguish fantasy from reality.", "advice_zh": "區分幻想與現實。", "image": "🌈", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Eight of Cups": {"name_zh": "聖杯八", "meaning": "Walking away, disillusionment, leaving behind.", "meaning_zh": "離開、幻滅、拋在身後。", "reversed": "Avoidance, fear of moving on, stagnation.", "reversed_zh": "逃避、害怕繼續前進、停滯。", "advice": "Have courage to walk away from what no longer serves you.", "advice_zh": "有勇氣離開不再服務你的事物。", "image": "🚶", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Nine of Cups": {"name_zh": "聖杯九", "meaning": "Contentment, satisfaction, gratitude, wish fulfilled.", "meaning_zh": "滿足、滿意、感恩、願望實現。", "reversed": "Inner happiness, materialism, dissatisfaction, smugness.", "reversed_zh": "內在幸福、物質主義、不滿、自滿。", "advice": "Appreciate your emotional fulfillment.", "advice_zh": "欣賞你的情感滿足。", "image": "😊", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Ten of Cups": {"name_zh": "聖杯十", "meaning": "Divine love, blissful relationships, harmony, alignment.", "meaning_zh": "神聖之愛、幸福關係、和諧、對齊。", "reversed": "Broken family, domestic conflict, misalignment.", "reversed_zh": "破碎家庭、家庭衝突、不對齊。", "advice": "Cherish your loving relationships.", "advice_zh": "珍惜你充滿愛的關係。", "image": "🏠", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Page of Cups": {"name_zh": "聖杯侍從", "meaning": "Creative opportunities, intuitive messages, curiosity, wonder.", "meaning_zh": "創造性機會、直覺訊息、好奇心、驚奇。", "reversed": "Emotional immaturity, creative block, insecurity.", "reversed_zh": "情感不成熟、創造力阻塞、不安全感。", "advice": "Embrace creative opportunities and listen to your intuition.", "advice_zh": "擁抱創造性機會並聆聽你的直覺。", "image": "🎨", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Knight of Cups": {"name_zh": "聖杯騎士", "meaning": "Romance, charm, imagination, beauty.", "meaning_zh": "浪漫、魅力、想像力、美麗。", "reversed": "Moodiness, disappointment, unrealistic expectations.", "reversed_zh": "情緒化、失望、不切實際的期望。", "advice": "Follow your heart but stay grounded.", "advice_zh": "跟隨你的心但要腳踏實地。", "image": "💘", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "Queen of Cups": {"name_zh": "聖杯皇后", "meaning": "Compassionate, caring, emotionally stable, intuitive.", "meaning_zh": "富有同情心、關懷、情感穩定、直覺。", "reversed": "Inner feelings, insecurity, dependence, martyrdom.", "reversed_zh": "內在感受、不安全感、依賴、殉道。", "advice": "Trust your emotional wisdom.", "advice_zh": "信任你的情感智慧。", "image": "👑", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},
    "King of Cups": {"name_zh": "聖杯國王", "meaning": "Emotional balance, compassion, diplomacy, control.", "meaning_zh": "情感平衡、同情心、外交手腕、控制。", "reversed": "Emotional manipulation, moodiness, coldness.", "reversed_zh": "情感操縱、情緒化、冷漠。", "advice": "Balance emotion with wisdom.", "advice_zh": "用智慧平衡情感。", "image": "🧙", "element": "Water", "suit": "Cups", "suit_zh": "聖杯"},

    # SWORDS SUIT (14 cards)
    "Ace of Swords": {"name_zh": "寶劍王牌", "meaning": "Breakthrough, clarity, sharp mind, truth.", "meaning_zh": "突破、清晰、敏銳心智、真理。", "reversed": "Confusion, miscommunication, chaos, blocked mental clarity.", "reversed_zh": "困惑、誤解、混亂、阻塞的心智清晰。", "advice": "Seek truth and mental clarity in your situation.", "advice_zh": "在你的處境中尋求真理和心智清晰。", "image": "⚔️", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Two of Swords": {"name_zh": "寶劍二", "meaning": "Difficult choices, indecision, stalemate, truce.", "meaning_zh": "困難選擇、猶豫不決、僵局、休戰。", "reversed": "Indecision, confusion, information overload.", "reversed_zh": "猶豫不決、困惑、信息超載。", "advice": "Make a decision even if it's difficult.", "advice_zh": "即使困難也要做出決定。", "image": "⚖️", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Three of Swords": {"name_zh": "寶劍三", "meaning": "Heartbreak, emotional pain, sorrow, grief.", "meaning_zh": "心碎、情感痛苦、悲傷、悲痛。", "reversed": "Recovery, forgiveness, moving on, healing.", "reversed_zh": "恢復、寬恕、繼續前進、療癒。", "advice": "Acknowledge your pain and allow yourself to grieve.", "advice_zh": "承認你的痛苦並允許自己悲傷。", "image": "💔", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Four of Swords": {"name_zh": "寶劍四", "meaning": "Rest, restoration, contemplation, recuperation.", "meaning_zh": "休息、恢復、沉思、復原。", "reversed": "Restlessness, burnout, stress, re-entering world.", "reversed_zh": "不安、精疲力盡、壓力、重新進入世界。", "advice": "Take time for mental rest and recovery.", "advice_zh": "花時間進行心智休息和恢復。", "image": "😴", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Five of Swords": {"name_zh": "寶劍五", "meaning": "Conflict, tension, defeat, win at all costs.", "meaning_zh": "衝突、緊張、失敗、不惜一切代價獲勝。", "reversed": "Reconciliation, resolution, moving on, learning from conflict.", "reversed_zh": "和解、解決、繼續前進、從衝突中學習。", "advice": "Consider if winning is worth the cost.", "advice_zh": "考慮勝利是否值得代價。", "image": "🏆", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Six of Swords": {"name_zh": "寶劍六", "meaning": "Transition, change, rite of passage, releasing baggage.", "meaning_zh": "過渡、改變、成年禮、釋放包袱。", "reversed": "Resistance to transition, unfinished business, stagnation.", "reversed_zh": "抗拒過渡、未完成的事務、停滯。", "advice": "Embrace necessary transitions.", "advice_zh": "擁抱必要的過渡。", "image": "⛵", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Seven of Swords": {"name_zh": "寶劍七", "meaning": "Deception, trickery, tactics, strategy.", "meaning_zh": "欺騙、詭計、戰術、策略。", "reversed": "Coming clean, rethinking approach, confession.", "reversed_zh": "坦白、重新思考方法、懺悔。", "advice": "Be strategic but honest in your approach.", "advice_zh": "在方法上要有策略但誠實。", "image": "🕵️", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Eight of Swords": {"name_zh": "寶劍八", "meaning": "Isolation, self-imposed restriction, imprisonment, powerlessness.", "meaning_zh": "孤立、自我限制、監禁、無力感。", "reversed": "New perspective, freedom, self-acceptance, release.", "reversed_zh": "新視角、自由、自我接納、釋放。", "advice": "Recognize that many limitations are self-imposed.", "advice_zh": "認識到許多限制是自我施加的。", "image": "🔗", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Nine of Swords": {"name_zh": "寶劍九", "meaning": "Anxiety, worry, fear, overwhelmed, nightmare.", "meaning_zh": "焦慮、擔憂、恐懼、不堪重負、噩夢。", "reversed": "Hope, reaching out, despair, mental torture.", "reversed_zh": "希望、尋求幫助、絕望、心智折磨。", "advice": "Share your worries with others.", "advice_zh": "與他人分享你的擔憂。", "image": "😨", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Ten of Swords": {"name_zh": "寶劍十", "meaning": "Betrayal, endings, crisis, painful lessons.", "meaning_zh": "背叛、結束、危機、痛苦教訓。", "reversed": "Recovery, regeneration, resisting an end, survival.", "reversed_zh": "恢復、再生、抗拒結束、生存。", "advice": "Accept endings as necessary for new beginnings.", "advice_zh": "接受結束作為新開始的必要條件。", "image": "🗡️", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Page of Swords": {"name_zh": "寶劍侍從", "meaning": "Curiosity, restlessness, mental energy, new ideas.", "meaning_zh": "好奇心、不安、心智能量、新想法。", "reversed": "Deception, manipulation, gossip, all talk.", "reversed_zh": "欺騙、操縱、閒話、空談。", "advice": "Stay curious but verify information.", "advice_zh": "保持好奇心但要驗證信息。", "image": "📚", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Knight of Swords": {"name_zh": "寶劍騎士", "meaning": "Ambitious, action-oriented, driven, communicative.", "meaning_zh": "有野心、行動導向、有動力、善於溝通。", "reversed": "Aggressive, ruthless, tactless, haste.", "reversed_zh": "侵略性、無情、不得體、匆忙。", "advice": "Act decisively but consider consequences.", "advice_zh": "果斷行動但要考慮後果。", "image": "⚡", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "Queen of Swords": {"name_zh": "寶劍皇后", "meaning": "Independent, unbiased judgment, clear boundaries, perceptive.", "meaning_zh": "獨立、公正判斷、清晰界限、洞察力。", "reversed": "Bitterness, coldness, cruelty, harsh judgment.", "reversed_zh": "痛苦、冷漠、殘酷、嚴厲判斷。", "advice": "Speak your truth with clarity and compassion.", "advice_zh": "以清晰和同情心說出你的真理。", "image": "👸", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},
    "King of Swords": {"name_zh": "寶劍國王", "meaning": "Mental clarity, intellectual power, authority, truth.", "meaning_zh": "心智清晰、智力力量、權威、真理。", "reversed": "Manipulative, cruel, weakness, abuse of power.", "reversed_zh": "操縱性、殘酷、軟弱、濫用權力。", "advice": "Use your mental clarity for truth and justice.", "advice_zh": "用你的心智清晰追求真理和正義。", "image": "🤴", "element": "Air", "suit": "Swords", "suit_zh": "寶劍"},

    # PENTACLES SUIT (14 cards)
    "Ace of Pentacles": {"name_zh": "錢幣王牌", "meaning": "Opportunity, prosperity, new financial beginning, manifestation.", "meaning_zh": "機會、繁榮、新財務開始、顯化。", "reversed": "Missed chance, lack of planning, poverty, false start.", "reversed_zh": "錯失機會、缺乏計劃、貧窮、錯誤開始。", "advice": "Take practical steps toward financial security.", "advice_zh": "採取實際步驟邁向財務安全。", "image": "💰", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Two of Pentacles": {"name_zh": "錢幣二", "meaning": "Balance, adaptability, time management, prioritization.", "meaning_zh": "平衡、適應性、時間管理、優先順序。", "reversed": "Overcommitted, disorganization, reprioritization.", "reversed_zh": "過度承諾、混亂、重新確定優先順序。", "advice": "Find balance in your responsibilities.", "advice_zh": "在你的責任中找到平衡。", "image": "🎪", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Three of Pentacles": {"name_zh": "錢幣三", "meaning": "Teamwork, collaboration, learning, implementation.", "meaning_zh": "團隊合作、協作、學習、實施。", "reversed": "Lack of teamwork, disorganized, poor planning.", "reversed_zh": "缺乏團隊合作、混亂、計劃不周。", "advice": "Collaborate with others for better results.", "advice_zh": "與他人合作以獲得更好結果。", "image": "👥", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Four of Pentacles": {"name_zh": "錢幣四", "meaning": "Conservation, frugality, security, control.", "meaning_zh": "節約、節儉、安全、控制。", "reversed": "Greed, materialism, self-protection, letting go.", "reversed_zh": "貪婪、物質主義、自我保護、放手。", "advice": "Find balance between saving and sharing.", "advice_zh": "在儲蓄和分享之間找到平衡。", "image": "💎", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Five of Pentacles": {"name_zh": "錢幣五", "meaning": "Isolation, worry, financial loss, poverty.", "meaning_zh": "孤立、擔憂、財務損失、貧窮。", "reversed": "Recovery, charity, spiritual poverty.", "reversed_zh": "恢復、慈善、靈性貧困。", "advice": "Seek help and community support.", "advice_zh": "尋求幫助和社區支持。", "image": "🚪", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Six of Pentacles": {"name_zh": "錢幣六", "meaning": "Generosity, charity, giving, receiving, sharing.", "meaning_zh": "慷慨、慈善、給予、接收、分享。", "reversed": "Strings attached, power trips, inequality, debt.", "reversed_zh": "附帶條件、權力炫耀、不平等、債務。", "advice": "Practice generosity without expectation.", "advice_zh": "實踐無期望的慷慨。", "image": "🎁", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Seven of Pentacles": {"name_zh": "錢幣七", "meaning": "Patience, harvest, reward, effort, assessment.", "meaning_zh": "耐心、收穫、獎勵、努力、評估。", "reversed": "Lack of growth, procrastination, impatience, wasted effort.", "reversed_zh": "缺乏成長、拖延、不耐煩、浪費努力。", "advice": "Be patient and trust the process.", "advice_zh": "耐心並信任過程。", "image": "🌱", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Eight of Pentacles": {"name_zh": "錢幣八", "meaning": "Apprenticeship, passion, high standards, skill development.", "meaning_zh": "學徒期、熱情、高標準、技能發展。", "reversed": "Perfectionism, lack of ambition, low standards, mediocrity.", "reversed_zh": "完美主義、缺乏野心、低標準、平庸。", "advice": "Dedicate yourself to learning and mastery.", "advice_zh": "專注於學習和精通。", "image": "🔨", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Nine of Pentacles": {"name_zh": "錢幣九", "meaning": "Luxury, self-sufficiency, financial independence, reward.", "meaning_zh": "奢華、自給自足、財務獨立、獎勵。", "reversed": "Self-worth, overspending, financial dependence.", "reversed_zh": "自我價值、過度消費、財務依賴。", "advice": "Enjoy your well-earned success.", "advice_zh": "享受你應得的成功。", "image": "🏡", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Ten of Pentacles": {"name_zh": "錢幣十", "meaning": "Wealth, family, establishment, inheritance, legacy.", "meaning_zh": "財富、家庭、建立、繼承、遺產。", "reversed": "Family conflict, financial failure, loss of security.", "reversed_zh": "家庭衝突、財務失敗、失去安全。", "advice": "Build a lasting legacy for future generations.", "advice_zh": "為後代建立持久遺產。", "image": "👨‍👩‍👧‍👦", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Page of Pentacles": {"name_zh": "錢幣侍從", "meaning": "Manifestation, financial opportunity, skill development.", "meaning_zh": "顯化、財務機會、技能發展。", "reversed": "Lack of progress, procrastination, learn from failure.", "reversed_zh": "缺乏進步、拖延、從失敗中學習。", "advice": "Embrace new learning opportunities.", "advice_zh": "擁抱新的學習機會。", "image": "📖", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Knight of Pentacles": {"name_zh": "錢幣騎士", "meaning": "Efficiency, hard work, responsibility, routine.", "meaning_zh": "效率、努力工作、責任、例行公事。", "reversed": "Laziness, boredom, feeling stuck, procrastination.", "reversed_zh": "懶惰、無聊、感到卡住、拖延。", "advice": "Stay consistent and methodical in your approach.", "advice_zh": "在方法上保持一致和有條不紊。", "image": "🐢", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "Queen of Pentacles": {"name_zh": "錢幣皇后", "meaning": "Nurturing, practical, providing security, generous.", "meaning_zh": "滋養、實際、提供安全、慷慨。", "reversed": "Self-care, smothering, financial independence.", "reversed_zh": "自我照顧、窒息、財務獨立。", "advice": "Nurture yourself and others practically.", "advice_zh": "實際地滋養自己和他人。", "image": "👸", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"},
    "King of Pentacles": {"name_zh": "錢幣國王", "meaning": "Wealth, business, leadership, security, abundance.", "meaning_zh": "財富、商業、領導力、安全、豐盛。", "reversed": "Financial failure, greed, arrogance, material instability.", "reversed_zh": "財務失敗、貪婪、傲慢、物質不穩定。", "advice": "Use your resources wisely and generously.", "advice_zh": "明智而慷慨地使用你的資源。", "image": "🤴", "element": "Earth", "suit": "Pentacles", "suit_zh": "錢幣"}
}

def get_tarot_reading(question, spread_type, language):
    """Generate a tarot reading based on question and spread type"""
    cards = random.sample(list(tarot_cards.items()), spread_type)
    reading = []
    
    for i, (card_name, card_data) in enumerate(cards):
        # Randomly determine if card is upright or reversed (30% chance of reversal)
        is_reversed = random.random() < 0.3
        
        # Choose language-specific content
        if language == 'zh':
            card_display_name = card_data["name_zh"]
            meaning = card_data["reversed_zh"] if is_reversed else card_data["meaning_zh"]
            advice = card_data["advice_zh"]
            suit = card_data["suit_zh"]
        else:
            card_display_name = card_name
            meaning = card_data["reversed"] if is_reversed else card_data["meaning"]
            advice = card_data["advice"]
            suit = card_data["suit"]
        
        reading.append({
            "card": card_display_name,
            "original_name": card_name,
            "meaning": meaning,
            "advice": advice,
            "image": card_data["image"],
            "reversed": is_reversed,
            "position": i + 1,
            "element": card_data["element"],
            "suit": suit
        })
    
    return reading

def main():
    # Initialize session state for language
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    
    # Language selector in sidebar
    with st.sidebar:
        lang = st.selectbox("🌐 Language / 語言", ["English", "中文"], index=0 if st.session_state.language == 'en' else 1)
        st.session_state.language = 'en' if lang == "English" else 'zh'
    
    # Get current language texts
    t = texts[st.session_state.language]
    
    # Elegant header
    st.markdown(f'<h1 class="main-header">{t["app_title"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="subtitle">{t["app_subtitle"]}</p>', unsafe_allow_html=True)
    
    # Sidebar with elegant design
    with st.sidebar:
        st.markdown(f"""
        <div style='text-align: center; padding: 20px 0;'>
            <div style='font-size: 3rem; margin-bottom: 10px;'>🌙</div>
            <h2 style='font-family: Cinzel, serif; color: #D4AF37;'>{t["sidebar_title"]}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown(f"""
        <div style='padding: 15px; background: rgba(212, 175, 55, 0.1); border-radius: 10px; margin: 10px 0;'>
            <h4 style='color: #D4AF37; font-family: Cinzel, serif;'>✨ {t["preparation"]}</h4>
            <p style='font-size: 0.9rem;'>{t["preparation_text"]}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='padding: 15px; background: rgba(212, 175, 55, 0.1); border-radius: 10px; margin: 10px 0;'>
            <h4 style='color: #D4AF37; font-family: Cinzel, serif;'>📜 {t["spread_meanings"]}</h4>
            <ul style='font-size: 0.9rem; padding-left: 20px;'>
                <li><strong>{t["spread_single"]}</strong></li>
                <li><strong>{t["spread_three"]}</strong></li>
                <li><strong>{t["spread_celtic"]}</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Shop link in sidebar
        st.markdown(f"""
        <div style='padding: 15px; background: rgba(212, 175, 55, 0.1); border-radius: 10px; margin: 10px 0;'>
            <h4 style='color: #D4AF37; font-family: Cinzel, serif;'>🛍️ {t["visit_shop"]}</h4>
            <p style='font-size: 0.9rem;'>{t["shop_text"]}</p>
            <a href="https://honorable-monarch-3bd.notion.site/journaling_the_universe-2843ea49e02c802bb483f23b7e6cb83d?source=copy_link" 
               target="_blank" class="store-link" style='display: block; text-align: center;'>
               🌟 {t["enter_shop"]}
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Deck information
        st.markdown(f"""
        <div style='padding: 15px; background: rgba(212, 175, 55, 0.1); border-radius: 10px; margin: 10px 0;'>
            <h4 style='color: #D4AF37; font-family: Cinzel, serif;'>🃏 {t["deck_info"]}</h4>
            <p style='font-size: 0.9rem;'>{t["deck_text"]}</p>
            <ul style='font-size: 0.8rem; padding-left: 20px;'>
                <li>{t["deck_major"]}</li>
                <li>{t["deck_minor"]}</li>
                <li>{t["deck_suits"]}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown(f"""
        <div style='text-align: center; color: #b8b8b8; font-size: 0.8rem;'>
            <p>{t["trust_intuition"]}</p>
        </div>
        """, unsafe_allow_html=True)

    # Main content area
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"### 🌟 {t['sacred_question']}")
        
        # Question input with elegant styling
        question = st.text_area(
            "",
            placeholder=t["question_placeholder"],
            height=150,
            help=t["preparation_text"]
        )
        
        # Spread selection with custom styling - FIXED VERSION
        st.markdown(f"### 📜 {t['choose_spread']}")
        
        # Define spread options directly without splitting
        spread_options = [
            (t["spread_single_option"], 1),
            (t["spread_three_option"], 3),
            (t["spread_celtic_option"], 5)
        ]
        
        spread_type = st.selectbox(
            "",
            spread_options,
            format_func=lambda x: x[0]
        )[1]
        
        # Elegant button
        if st.button(f"🌀 {t['consult_oracle']}", use_container_width=True):
            if question.strip():
                with st.spinner("🌀 The veil parts... wisdom emerges..." if st.session_state.language == 'en' else "🌀 帷幕分開...智慧顯現..."):
                    # Add a small delay for dramatic effect
                    import time
                    time.sleep(2)
                    # Generate reading
                    reading = get_tarot_reading(question, spread_type, st.session_state.language)
                    st.session_state.reading = reading
                    st.session_state.question = question
                    st.session_state.timestamp = datetime.datetime.now()
                    st.rerun()
            else:
                st.warning(f"💫 {t['focus_intention']}")
    
    with col2:
        if 'reading' in st.session_state:
            # Display reading with elegant layout
            st.markdown(f"## 🔮 {t['cards_spoken']}")
            
            # Question and timestamp in elegant box
            st.markdown(f"""
            <div class="question-box">
                <h4 class="gold-text">{t['sacred_question']}</h4>
                <p style='font-size: 1.1rem; font-style: italic;'>"{st.session_state.question}"</p>
                <p class="silver-text" style='font-size: 0.9rem; margin-top: 10px;'>
                {t['reading_cast']} {st.session_state.timestamp.strftime("%Y-%m-%d %H:%M")}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Cards display
            st.markdown(f'<div class="spread-title">{t["sacred_spread"]}</div>', unsafe_allow_html=True)
            
            # Create columns for cards
            cols = st.columns(len(st.session_state.reading))
            
            # Position names based on spread type
            if len(st.session_state.reading) == 1:
                position_names = [t["position"] + " 1"]
            elif len(st.session_state.reading) == 3:
                if st.session_state.language == 'en':
                    position_names = ["Past Influence", "Current Situation", "Future Path"]
                else:
                    position_names = ["過去影響", "當前狀況", "未來道路"]
            else:  # 5 cards
                if st.session_state.language == 'en':
                    position_names = ["Present Situation", "Immediate Challenge", "Distant Past", "Recent Past", "Potential Outcome"]
                else:
                    position_names = ["當前狀況", "立即挑戰", "遙遠過去", "近期過去", "潛在結果"]
            
            for i, (col, card) in enumerate(zip(cols, st.session_state.reading)):
                with col:
                    position_name = position_names[i] if i < len(position_names) else f"{t['position']} {i+1}"
                    status_class = "reversed" if card["reversed"] else "upright"
                    status_text = "Reversed" if card["reversed"] else "Upright" if st.session_state.language == 'en' else "逆位" if card["reversed"] else "正位"
                    
                    st.markdown(f"""
                    <div class="tarot-card">
                        <div class="card-image">{card['image']}</div>
                        <div class="card-name">{card['card']}</div>
                        <div style='color: #b8b8b8; font-size: 0.9rem; margin: 5px 0;'>{position_name}</div>
                        <div class='{status_class}' style='font-size: 0.8rem;'>{status_text}</div>
                        <div style='color: #888; font-size: 0.8rem; margin-top: 8px;'>
                        {t['suit']}: {card['suit']} • {t['element']}: {card['element']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Divider
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            
            # Detailed interpretations
            st.markdown(f"## 📖 {t['sacred_interpretations']}")
            
            for i, card in enumerate(st.session_state.reading):
                position_name = position_names[i] if i < len(position_names) else f"{t['position']} {i+1}"
                
                st.markdown(f"""
                <div class="interpretation-box">
                    <h4 class="gold-text">#{i+1} • {position_name}</h4>
                    <h3 style='color: #D4AF37; margin: 10px 0;'>{card['image']} {card['card']} 
                    <span style='font-size: 1rem;' class='{"reversed" if card["reversed"] else "upright"}'>
                    ({"Reversed" if card["reversed"] else "Upright" if st.session_state.language == 'en' else "逆位" if card["reversed"] else "正位"})</span>
                    </h3>
                    <p><strong class="gold-text">{t['suit']}:</strong> {card['suit']} • <strong class="gold-text">{t['element']}:</strong> {card['element']}</p>
                    <p><strong class="gold-text">{t['meaning']}:</strong> {card['meaning']}</p>
                    <p><strong class="gold-text">{t['guidance']}:</strong> {card['advice']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Final guidance
            st.markdown(f"## 💫 {t['cosmic_guidance']}")
            st.markdown(f"""
            <div style='background: rgba(212, 175, 55, 0.1); padding: 25px; border-radius: 12px; border: 1px solid #D4AF37;'>
                <h4 style='color: #D4AF37; text-align: center; font-family: Cinzel, serif;'>
                🌟 {t['truths']} 🌟
                </h4>
                <p style='text-align: center; font-style: italic; margin: 15px 0;'>
                {t['truth_text']}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Download button
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button(f"📜 {t['save_reading']}", use_container_width=True):
                    reading_text = f"""
                    {t['app_title']}
                    {'='*len(t['app_title'])}
                    
                    {t['reading_cast']}: {st.session_state.timestamp.strftime("%Y-%m-%d %H:%M")}
                    {t['sacred_question']}: {st.session_state.question}
                    
                    {t['cards_spoken']}:
                    {''.join([f'''
                    {card['position']}. {card['card']} ({'Reversed' if card['reversed'] else 'Upright'})
                       {t['position']}: {position_names[card['position']-1] if card['position']-1 < len(position_names) else 'General'}
                       {t['suit']}: {card['suit']} • {t['element']}: {card['element']}
                       {t['meaning']}: {card['meaning']}
                       {t['guidance']}: {card['advice']}
                    ''' for card in st.session_state.reading])}
                    
                    {t['cosmic_guidance']}:
                    {t['truth_text']}
                    
                    {t['disclaimer']}
                    """
                    
                    st.download_button(
                        label=f"📥 {t['download_record']}",
                        data=reading_text,
                        file_name=f"tarot_reading_{st.session_state.timestamp.strftime('%Y%m%d_%H%M')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
        
        else:
            # Beautiful initial state with properly styled shop promotion
            st.markdown(f"""
            <div style='text-align: center; padding: 40px 20px;'>
                <div style='font-size: 5rem; margin-bottom: 20px;'>🔮</div>
                <h2 style='color: #D4AF37; font-family: Cinzel, serif;'>{t['cards_await']}</h2>
                <p style='color: #b8b8b8; font-size: 1.1rem; margin: 20px 0;'>
                {t['instructions']}
                </p>
                <div style='color: #666; font-style: italic; margin-top: 30px;'>
                <p>✨ {t['trust_process']} ✨</p>
                <p>✨ {t['listen_intuition']} ✨</p>
                <p>✨ {t['embrace_wisdom']} ✨</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Properly integrated shop promotion
            st.markdown(f"""
            <div class="shop-promotion">
                <h4 style='color: #D4AF37; font-family: Cinzel, serif; text-align: center;'>📓 {t['continue_journey']}</h4>
                <p style='color: #b8b8b8; text-align: center;'>{t['shop_promo']}</p>
                <div style='text-align: center;'>
                    <a href="https://honorable-monarch-3bd.notion.site/journaling_the_universe-2843ea49e02c802bb483f23b7e6cb83d?source=copy_link" 
                       target="_blank" class="store-link">
                       🛍️ {t['enter_shop']}
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Elegant footer with shop link
    st.markdown(f"""
    <div style='text-align: center; margin-top: 50px; padding: 20px; color: #666; border-top: 1px solid #333;'>
        <p>{t['footer_text']}</p>
        <p style='font-size: 0.9rem; margin: 15px 0;'>
            <a href="https://honorable-monarch-3bd.notion.site/journaling_the_universe-2843ea49e02c802bb483f23b7e6cb83d?source=copy_link" 
               target="_blank" style='color: #D4AF37; text-decoration: none; font-family: Cinzel, serif;'>
               🌟 {t['visit_shop_footer']}
            </a>
        </p>
        <p style='font-size: 0.8rem;'>{t['disclaimer']}</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

