> [!NOTE]
>
> ## 🌐 Website Availability
>
> ⚠️ The website is currently unavailable as it has been taken down from production.
> If you need access, please contact me, and I can redeploy the site.

# Store API project

This project features a store API developed with Django.

You can explore the website and API using the links below:

https://maayan-store-345656c6f6fd.herokuapp.com/

<img src="https://github.com/MaayanBah/storefront/blob/ebdf53b7b3f79f52621c6690bd41ee4fde2e9d38/github_images/homepage.png" alt="Image Alt Text" width="400"/>

https://maayan-store-345656c6f6fd.herokuapp.com/store/

<img src="https://github.com/MaayanBah/storefront/blob/ebdf53b7b3f79f52621c6690bd41ee4fde2e9d38/github_images/store.png" alt="Image Alt Text" width="400"/>

## Login

In order to create a user you can send a POST request to this URL (visit this URL for details):

https://maayan-store-345656c6f6fd.herokuapp.com/auth/users/

You can login from this URL and you will get a refresh token and an access token (which is valid for 1 hour):

https://maayan-store-345656c6f6fd.herokuapp.com/auth/jwt/create

Then you add the access token to your header (key: "Authorization", value: "JWT ${access_token}")

## Superuser

The superuser can login from this URL:

https://maayan-store-345656c6f6fd.herokuapp.com/admin/

When accessed, the superuser can view, delete and modify the API models:

<img src="https://github.com/MaayanBah/storefront/blob/3655441453f650ff2277310a2b1429616284ffb2/github_images/admin.png" alt="Image Alt Text" width="500"/>

For example this is the products page:

<img src="https://github.com/MaayanBah/storefront/blob/3655441453f650ff2277310a2b1429616284ffb2/github_images/admin_prod.png" alt="Image Alt Text" width="700"/>
