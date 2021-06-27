# Timesheet-Why-
Учебный pet-project для 3го модуля курса "Архитектор ПО"

Приложение "Таймшит Зачем?" позволяет вести учет временных затрат на проекты, расчитывать стоимость и учитывать оплаты, полученные от заказчика. Отличительная особенность данного приложения заключается в том, что при учете временных затрат обызательно указывается цель каждой из проделанных работ. Ответ на вопрос "Зачем?" позволяет исполнителю осознать для чего нужна каждая из работ, а заказчику понимать, за что именно он платит.

На практике достаточно часто сталкивалась с такой ситуацией, что заказчик выдает задание, а исполнитель его механически выполняет, не пытаясь понять для чего это надо. Данный подход допустим в операционной деятельности, но в случае проектного подхода может привести к провалу. Это объясняется тем, что заказчик и исполнитель могут под одними и теми же словами понимать совершенно разные вещи, заказчик может не всегда релевантно своим потребностям составить задние, а исполнитель, понимающий цель работы может предложить более простое и менее трудозатратное решение.

Прототип такого приложения уже существует в виде книги Excel почти 1,5 года и успел зарекомендовать себя лучшим образом. К идее подобного подхода меня подталкнула ценность, которая продвигалась в компании, где я работаю "Мысли как предпринимать" - свою рабочаю деятельность необходимо вести осмысленно и беспрестанно оценивать на предмет возможных улучшений. То есть при выполнении даже рутинных задач стоит задавать себе (и начальнику=заказчику) вопрос "А зачем я это делаю?", "Могу ли я это сделать эффективнее или даже не делать, при этом достигнув изначальной цели?".

Приложение "Таймшит Зачем?" позволяет вести учет рабочего времени в разрезе проектов и типов работ, с указание выходных документов. Кроме этого, приложение позволяет вести финансовый учет работ над проектами с учетом разных почасовых ставок для разных работ и проектов, а благодаря ведению фактических выплат держать под контролем задолженности по оплате работ над проектом.

Таким образом, в данном репозитории собрана вся информация касательно приложения "Таймшит Зачем?": от описания приложения и схем, до кода реализации.

Приложение "Таймшит Зачем?" представляет собой клиент-серверное web-приложение MPA (Multi Page Application) на базе паттерна MVC (model-view controller). 
Данные выбор объясняется тем, что:
1. Дальнейшее развитие приложения возможно как добавления нового типа пользователей "Заказчик", с определенной видимостью элементов (заказчик видит только данные по своему проекту) и определенными возможностями к действию (заказчик может только просматривать записи, но не создавать или редактировать их).
2. Многопользовательский режим работы (один исполнитель работает над двумя и более проектами, а заказчики просматривают информацию).
3. Приложение должно быть доступно "всегда и везде", для этого не подходит толстый клиент (SPA - Single Page Application), так как он требует установки на компьютер, что не позволит получить доступ к данным быстро.
4. Приложение должно отвечать клиент-серверной архитектуре, так как при хранении данных на определенном компьютере данными нельзя будет воспользоваться без доступа к компьютеру.
5. Если приложение будет мобильным, то им нельзя будет пользоваться на компьютере, что не очень удобно, так как подразумевается достаточно большое количество текста и ссылки на документы.
