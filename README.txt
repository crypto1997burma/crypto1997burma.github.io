CRYPTO 1997 WEBSITE — စတင်အသုံးပြုနည်း

ပါဝင်သည့်ဖိုင်
- index.html : Website တစ်ခုလုံး (ဖုန်း/ကွန်ပျူတာနှစ်မျိုးလုံးအတွက် responsive)
- Crypto ဈေးနှုန်း: CoinGecko public API မှ BTC, ETH, SOL, XRP live data ရယူရန် ကြိုးစားသည်။
  API ကန့်သတ်ချက်၊ Internet သို့မဟုတ် browser ပြဿနာကြောင့် တစ်ခါတစ်ရံ မပြနိုင်ပါ။
- Facebook ချိတ်ဆက်ရန်: index.html ကို text editor ဖြင့်ဖွင့်ပြီး
  const FACEBOOK_PAGE_URL = "https://www.facebook.com/";
  အစား သင့် Page URL ကို ထည့်ပါ။

အခမဲ့ Online တင်နည်း (Cloudflare Pages)
1. GitHub account တစ်ခုဖွင့်ပါ: https://github.com/
2. New repository ကိုနှိပ်ပြီး crypto1997-website လို့နာမည်ပေးပါ။
3. index.html ကို repository ထဲ Upload files ဖြင့်တင်ပြီး Commit changes နှိပ်ပါ။
4. Cloudflare account ဖွင့်ပါ: https://dash.cloudflare.com/sign-up
5. Workers & Pages > Create application > Pages > Connect to Git ကိုရွေးပါ။
6. GitHub ကိုချိတ်ပြီး crypto1997-website repository ကိုရွေးပါ။
7. Plain HTML ဖြစ်လို့ Framework preset မရွေး၊ Build command ကို ဗလာထားပါ။
   Build output directory ကို / (root) ထားပြီး Deploy နှိပ်ပါ။
8. Deploy ပြီးလျှင် Cloudflare ပေးတဲ့ *.pages.dev URL နဲ့ ဝင်ကြည့်နိုင်ပါသည်။

မှတ်ချက်:
- Website ကို အွန်လိုင်းတင်ရန် သင့် GitHub/Cloudflare အကောင့်တွင် သင်ကိုယ်တိုင် Sign in လုပ်ရပါမည်။
- အခမဲ့ subdomain သုံးနိုင်ပြီး ကိုယ်ပိုင် .com domain က သီးခြားကုန်ကျနိုင်ပါသည်။
- လက်ရှိသတင်းကတ်များသည် အစပြုရန် နမူနာ/ပညာပေးအကြောင်းအရာများဖြစ်သည်။ သတင်းအသစ်များကို ကိုယ်တိုင်စစ်ဆေးပြီး update လုပ်ပါ။
- ဤ website သည် ရင်းနှီးမြှုပ်နှံမှုအကြံပေးဝန်ဆောင်မှု မဟုတ်ပါ။
