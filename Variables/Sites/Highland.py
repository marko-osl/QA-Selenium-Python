
# VALUES
firstName = "Marek"
lastName = "Test"
question = "How I can write the best test in Selenium & Python?"
wrongEmail = "WrongEmail"

# CONTACT FORM - HOMEPAGE
firstNameOnHomepage = "first_name"
lastNameOnHomepage = ".pl_widget-contact--name #last_name"
emailContactFormOnHomepage = ".pl_widget-contact--email #email"
phoneNumberContactFormOnHomepage = ".pl_widget-contact--phone #phone"
questionContactFormOnHomepage = ".pl_widget-contact--questions #question"
submitButtonContactFormOnHomepage = ".pl_widget-contact-column-right input[type='submit']"
successSendingContactFormOnHomepage = '//*[@id="contact"]/div/div[2]/section/div[1]/h4'
firstNameErrorOnHomepage = "/html//p[.='Your name is required.']"
phoneNumberErrorOnHomepage = "/html//p[.='A valid phone is required.']"
emailErrorOnHomepage = "/html//p[.='A valid email is required.']"
questionErrorOnHomepage = "/html//textarea[@id='question']"

# CONTACT FORM - CONTACT PAGE
contactPageLinkMenu = "#menu-primary [href='\/contact']"

# SIGNUP FORM
registerButton = ".pl_header-content .pl_register_lead_link"
registerFirstNameInput = '.pl_wrapper--open .js-form-content .reg_form_first_name  input[name="first_name"]'
registerLastNameInput = '.pl_wrapper--open .js-form-content .reg_form_last_name  input[name="last_name"]'
registerEmailInput = '.pl_wrapper--open .js-form-content .reg_form_email  input[name="email"]'
registerPasswordInput = '.pl_wrapper--open .reg_form_pass input[name="password"]'
registerConfirmPasswordInput = '.pl_wrapper--open .reg_form_confirm_pass input[name="confirm"]'
registerSignUpButton = '.pl_wrapper--open .js-form-content .pl_submit-wrapper input[value="Register"]'
registerVerifyHandle = ".pl_nav-wrapper .pl_lead_profile_link"
registerLogOutButton = ".pl_nav-wrapper a.pl_logout_link"
registerEmailExistingMessage = "//p[contains(text(),'This email is already in use.')]"
registerFirstNameWrongMessage = "//p[contains(text(),'A valid first name is needed.')]"
registerLastNameWrongMessage = "//p[contains(text(),'A valid last name is needed.')]"
registerEmailWrongMessage = "//p[contains(text(),'A valid email is needed.')]"
registerPasswordWrongMessage = "//p[contains(text(),'Please enter a password.')]"
registerConfirmPasswordWrongMessage = "//p[contains(text(),'Please confirm your password.')]"

# SIGNIN FORM
loginButton = '//*[@id="header"]/div/div[3]/div[2]/a[1]'
loginEmailInput = '.pl_wrapper--open .js-form-content .login-email  input[name="email"]'
loginPasswordInput = '.pl_wrapper--open .login-password input[name="password"]'
loginSignInButton = '.pl_wrapper--open .js-form-content .pl_submit-wrapper input[value="Log In"]'
loginVerifyHandle = '.pl_lead_profile_link'
loginNotExistingAccountMessage = "#pl_login > .js-pl_membershipForm > #pl_login_form_inner_wrapper > div[style='display: block;']"
loginPasswordEmptyMessage = '.pl_wrapper--open .login-password input[name="password"]'
loginEmailEmptyMessage = '.pl_wrapper--open .js-form-content .login-email  input[name="email"]'

# FORGOT PASSWORD
forgotPasswordLoginLink = '//*[@id="header"]/div/div[3]/div[2]/a[1]'
forgotPasswordButton = ".pl_popup-wrapper #pl_login #pl_login_form_inner_wrapper .js-form-content .login-submit .pl_password_link "
forgotPasswordEmailInput = '.pl_wrapper--open .js-form-content .login-email  input[name="email"]'
forgotPasswordResetPasswordButton = '.pl_wrapper--open .js-form-content .pl_submit-wrapper input[name="submit"]'
forgotPasswordSuccessHandle = '.pl_popup-wrapper #pl_loginReset .js-pl_membershipForm .success'
forgotPasswordEmptyEmailMessage = "/html//p[.='A valid email is needed']"
forgotPasswordExitButton = ".pl_btn--close"