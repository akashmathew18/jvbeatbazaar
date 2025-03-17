function onSignIn(googleUser ) {
    var profile = googleUser .getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail());

    // You can send the ID token to your server for verification
    var id_token = googleUser .getAuthResponse().id_token;
    // Send the ID token to your server with an AJAX request
}