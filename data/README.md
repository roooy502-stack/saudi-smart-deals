# قاعدة المنتجات

ملف `products.json` هو مصدر البيانات الوحيد للبطاقات. كل عنصر يجب أن يحتوي على `id`, `name`, `store`, `category_id`, `category_name`, `description`, `price`, `currency`, `affiliate_url`, `last_checked`, و`demo`.

- استخدم `demo: true` مع أي بيانات توضيحية.
- لا تضع رابط إحالة قبل قبولك في البرنامج التابع.
- لا تضع سعراً أو خصماً دون مصدر موثق وتاريخ تحقق.
- استخدم `affiliate_url: "#"` عندما لا يوجد رابط معتمد.
