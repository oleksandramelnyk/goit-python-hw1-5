'''На данные момент у нас есть три переменные: first_name, last_name и full_name

Добавим переменную message, которая фактически будет прототипом шаблонного письма пользователю, купившему билет. 
Эту переменную мы сформируем с помощью f-строки. В переменную message мы, с помощью f-строки, поместим строку следующего содержания:

"Уважаемый <подставляем здесь first_name>, мы сообщаем вам, что вы приобрели билет для путешествия на остров Маврикий. 
Отправление 31 июня сего года. Просьба обратится за билетом в кассу аэропорта. При себе иметь паспорт на <подставляем здесь full_name>. 
С нетерпением ожидаем вас."'''

first_name = "Yurii"
last_name = "Kuchma"
full_name = first_name + " " + last_name

message = f'Уважаемый {first_name}, мы сообщаем вам, что вы приобрели билет для путешествия на остров Маврикий. Отправление 31 июня сего года. Просьба обратится за билетом в кассу аэропорта. При себе иметь паспорт на {full_name}. С нетерпением ожидаем вас.'
