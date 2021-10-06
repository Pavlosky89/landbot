This document contains the development process involved in this project

**Architecture:**

The structure was planned as a hexagonal design, using adapters, interfaces, services and entities or models.

**Models:**

Using the existing model of Users provided by Django, a new model called "CustomUser" was created in order to add the fields "phone" and "name".
Also, the username was modified for using the email as id.

The Notification model acts like a log of all the notifications sent to the product department, with the username of who asked the bot, the channel of communication, and the topic.

**Adapters:**

There are two endpoints available, one to register users and the other, to send notifications.
- app/create_user 

request example:

        {"name":"landbottest", "email":"landbottest@bot.com","phone":"111222333"}
- app/send_notifications

request example:

        {"username":"landbottest@bot.com","topic":"sales"}

**Services:**

Contains the use cases and acts as the bridge between the request and the data models. Is where the input get processed and checked if it is valid or not.

For one hand, there is the user_registration_service, who is in charge of calling the operation "create" of the model CustomUser. After that, launches the task "send_email" on Celery

On the other hand, the notification_service gets the info related to the user, using a method from the previous service: "get_name_by_username".

After that, depending on the topic asked by the user, there are two possibilities:

- "pricing": sends an email to the product department with the name of the user and the topic.
- "sales": sends a message through Whatsapp, to the phone number of the product department with the same info.

Those behaviours are stored in a configuration file inside the "utils" directory, to easy change them if needed, without changing the code.