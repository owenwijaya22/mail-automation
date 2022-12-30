# mail-automation

by **Owen Valentinus**

A Python library for batch receiving/sending emails with various features, asynchronously

## Explanations regarding the project

* Made with custom domain registrar, kaid3n.me, on namecheap. (<https://ap.www.namecheap.com/domains/domaincontrolpanel/kaid3n.me/domain>)

* Hosted on DigitalOcean  with auto-scaling VPS droplet on CentOS 9 Stream x64. (<https://cloud.digitalocean.com/networking/domains/mailgun.kaid3n.me?i=efa6aa>)
-current scaling is at 1 GB RAM, 25 GB NVME SSD, i5 vCPU
-will include docker and kubernetes for storing and managing the application containers

* Provides both ipv4 for standard address space and ipv6   for larger and faster loading speed.

* Uses self-made DNS records so that site redirections are secure and trusted, such as:
  * MX records for specifying the mail server responsible for accepting email responses.
  * CNAME records for mapping subdomains and multiple hostnames to the true domain name.
  * Private A record for mapping the urls to a private ip address.

* Utilizes mailgun API and STMP for sending emails.

## INSTALLATION

To be published in the future on PyPI, so that it can be installed with pip, i.e.,

```powershell
pip install mail_automation
```

## USAGE

*more features are to be added in the future

```python
import mail_automation

"""send message on a specific time"""
mail_automation.send_scheduled(subject='foo', text='bar', recipient='hansv149@gmail.com', date='MM DD hh:mm:ss')

"""send a single message to a single recipient"""
mail_automation.send(subject='foo', text='bar', recipient='hansv149@gmail.com')

"""send the same email to a bunch of people"""
"""will be asked for multiple inputs with prompts to select recipients"""
mail_automation.spam(subject='foo', text='bar')

"""send a single image to a single recipient"""
mail_automation.attach(subject='foo', text'bar', attachment_path='your/image/path', recipient='hansv149@gmail.com')

"""send the same attachment to a bunch of people"""
"""will be asked for multiple inputs with prompts to select recipients"""
mail_automation.spam_attach(subject='foo', text='bar', attachment_path='your/image/path')
```

## CONTRIBUTING

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## TESTS

`git clone https://github.com/owenwijaya22/mail-automation.git`

Run `py -m tests.test` from  `mail-automation` directory

## LICENSE

MIT License

Copyright (c) [2022] [Owen Valentinus]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
