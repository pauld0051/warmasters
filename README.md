# WARMASTERS

Warmasters is a near-real-time role playing game. Users can control how much time they advance to create a continuous game play solution.

## Testing Webhooks

### NGROK Method

    1. For a Windows based VS Code download the ngrok zip file from ngrok
    2. Unzip and run ngrok anywhere (it's stand-alone)
    3. type ngrok.exe http [your local server port] (I use 5000, but you might be using 8000 which is common)
    4. Get the https address that is assigned to you
    5. Add that to the hosts in settings.py - ALLOWED_HOSTS = [your_number_here.ngrok.io"]
    6. Add your Webhook to Stripe the same way as the video for eg: https://your_ngrok_site.ngrok.io/checkout/wh/
    7. Send a webhook following the video and check the terminal for success!

### Stripe CLI Method (preferred)

    Download the latest Stripe CLI and put it in an easy directory to access on your main computer drive

    The following is for Windows based computers:

    To install the Stripe CLI on Windows:

    1. Download the latest windows zip file from https://github.com/stripe/stripe-cli/releases/latest
    2. Unzip the stripe_X.X.X_windows_x86_64.zip file
    3. Run the unzipped .exe file in your terminal

    From there follow the instructions: https://stripe.com/docs/stripe-cli/webhooks#forward-events

Django's secret key: https://djecrety.ir/
