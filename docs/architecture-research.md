# بحث المعمارية المجانية

## القرار

أفضل نقطة بداية لهذا المشروع هي موقع ثابت بلا خادم: HTML وCSS وJavaScript وJSON، مستضاف على GitHub Pages، مع GitHub Actions للفحص والنشر والتقارير. هذا الخيار لا يحتاج قاعدة بيانات أو مفتاح API، ويقلل متطلبات جهاز Windows 10 ذي الذاكرة المحدودة. يمكن ترقية المعمارية لاحقاً فقط إذا ظهرت حاجة فعلية مثل لوحة إدارة أو مصدر بيانات مصرح به.

## لماذا GitHub Pages؟

توضح وثائق GitHub أن Pages يدعم النشر عبر workflows مخصصة، وأن المسار الرسمي يعتمد على `configure-pages` و`upload-pages-artifact` و`deploy-pages`. كما تتطلب وظيفة النشر صلاحيات `pages: write` و`id-token: write` وبيئة نشر منفصلة [1]. لذلك يستخدم هذا المستودع أقل صلاحيات عملية، ولا يطلب أسراراً.

## لماذا GitHub Actions للصيانة؟

تدعم Actions تشغيل workflow عند push وpull request وبجدول cron. وتوضح وثائق الصياغة أن `concurrency` يمنع تشغيل نسخ متعارضة من workflow في الوقت نفسه [2]. لذلك يحتوي المشروع على فحوص مستقلة للبيانات وSEO والروابط، وتقرير صيانة مجدول، مع تشغيل يدوي عند الحاجة.

## لماذا JSON بدلاً من API أو قاعدة بيانات؟

ملف JSON يمكن مراجعته عبر Git، وفحصه قبل النشر، وتعديله من جهاز ضعيف. هذا لا يجلب أسعاراً تلقائياً ولا يتجاوز قيود أي متجر. يجب على المالك إدخال البيانات المسموح بها فقط، مع تاريخ تحقق واضح. البيانات المرفقة في البداية موسومة `DEMO_ONLY` ولا تمثل عروضاً حقيقية.

## SEO والبيانات المنظمة

تشرح Google أن صفحات المنتجات التحريرية التي لا يتم الشراء منها مباشرة يمكن أن تستخدم Product snippets، وأن البيانات المنظمة قد تساعد Google على فهم السعر والتوفر والمراجعات، لكنها لا تضمن ظهور النتيجة الغنية [3]. لهذا يبقى المشروع صادقاً: لا يضيف مراجعات أو سعراً أو توفرًا غير موجود في المصدر، وتظل إضافة structured data الحقيقية خطوة لاحقة مرتبطة ببيانات موثقة.

## حدود الحل

GitHub Pages لا يوفر لوحة تحكم أو تحديث أسعار تلقائياً. النشر المجاني لا يضمن زيارات أو عمولات. يجب الحصول على موافقة برنامج إحالة، احترام شروط استخدام المتاجر، استخدام الصور والروابط المسموح بها، وكتابة إفصاح واضح وسياسة خصوصية مخصصة قبل التشغيل التجاري.

## المصادر

[1]: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages "Using custom workflows with GitHub Pages"
[2]: https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions "Workflow syntax for GitHub Actions"
[3]: https://developers.google.com/search/docs/appearance/structured-data/product "Product structured data"
