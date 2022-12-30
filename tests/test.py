from mail_automation.send_message import MailAutomation
bot = MailAutomation()
print(bot.send('text', 'hm','owenwijaya89@gmail.com').status_code)