# RSS Project

![Project main screen](/doc-images/index-above-the-fold.png)

[RSS](https://ci-igor-rss.herokuapp.com/) is an application for managing restaurant table reservations. It allows a customer to register with the system and make, list, cancel and change reservations for a choosen date and time and for specific table or tables. It also allows an admin user to take bookings for any customer and register them on the system, edit, cancel and see all bookings.

The main landing page presents the user with a button to make a reservation and links to information about the place, galery of images and downloadable menu.

![Project main page](/doc-images/whole-index-page.png)

## Features

### **User Registration and Logging-in**
A user can register with the system and then log-in in order to gain access to the booking feature. If users are not logged in and proceed to the booking page they will be asked to log-in or register

![User registration page](/doc-images/register.png)
![Log in page](/doc-images/login.png)

### **Booking**
After a successful logging to the system a user can make a new booking, see all his/hers bookings and delete them or amend.  Similarily and admin user is presented with very similar functionality except that an admin can see all the bookings and make reservation to any user, also not registered on the system.

![Regular User Booking](/doc-images/user-booking-form.png)
![Admin Booking](/doc-images/admin-booking-form.png)

Only available tables for a given date and time slot combination are made available for selection.

![Admin Booking](/doc-images/available-tables-only.png)

### **Booking Amendments**
Edition of a booking is accessed by a edit button in a table listing all bookings. A pre-populated form is displayed and user can make and confirm changes. This is also different for a regular and an admin user.

![Edit Form](/doc-images/edit-booking.png)

### **Booking Cancelation**
In the same way as editing a deletition of a booking is made by clicking an icon in the bookings listing. A dialog is displayed allowing user either confim or cancel the action. Additionaly a listing of bookings for the admin shows a button alowing the admin to delete all expierd bookings if they exist.

![Confirmation dialog](/doc-images/confirmation-dialog.png)

### **Administrator features**
An admin can acces all bookings and users via the /admin panel and do any arbitrary changes.

## **Testing**

- I tested the website in Firefox, Safari, Chrome and Edge browsers. Both responsiveness and integrity of the layouts were checked. The website worked in all four browsers without any problems.
- I confirmed that all texts a legible in both on mobile and desktop computers.
- All hyperlinks were checked and link to the desired detinations.
- The booking feature was extensively tested by manually entering the data, both as a regular and admin user.
- The listing of bookings was checked against the actual list of bookings in the admin page.
- Both the edit and delete features were tested by clicking appropriate links and checking if the results were recorded in the database (both with the admin panel and the database itself)

### Bugs
All noticed bugs were fixed.
There are no known bugs remaining.

## **Deployment**

To deploy this application on Heroku:

1. Log in to Heroku and proceed to dashboard
2. Select to create new app and give it a name and select region, press **Create app** button
3. In the Settings tab in the Config vars click **Reveal Config vars** and add the following:
    - key *PORT* and value *8000*
    - key *DATABASE_URL* and value *Link to your postgress database*
    - key *HOST_NAME* and value *URL of your app on Heroku* (listed below in the Domains section)
    - key *SECRET_KEY* and value *A secret key for your app*
4. In the buildpacks section add *heroku/python*
5. Go to the **Deployment** tab go to **Deployment method** section and select **Github**. Connect to you github account if asked
6. Search for the repository containing this app and connect to it
7. Either using **Automatic deploys** or **Manual deploy** select the branch (usually main) and press **Deploy Branch** button

## Credits

C.I. gitpod template for Heroku app deployments
The template for the website coms from [startbootstrap.com](https://startbootstrap.com/theme/creative)

## **Media**
Images are from [Freepik](https://www.freepik.com/)
