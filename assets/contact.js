/* Contact form. EmailJS keys go here and nowhere else.
   1. emailjs.com account, add an email service and a template
   2. paste the three values below
   3. template variables available: from_name, reply_to, phone, preferred_contact, message */
(function () {
  'use strict';

  var CFG = {
    publicKey:  'EMAILJS_PUBLIC_KEY',
    serviceId:  'EMAILJS_SERVICE_ID',
    templateId: 'EMAILJS_TEMPLATE_ID'
  };

  var form = document.getElementById('contactForm');
  if (!form) return;
  var status = document.getElementById('f-status');
  var btn = document.getElementById('f-send');

  function say(kind, text) {
    status.className = 'form-status on ' + kind;
    status.textContent = text;
  }
  function flag(input, bad) {
    input.closest('.field').classList.toggle('err', bad);
    input.setAttribute('aria-invalid', bad ? 'true' : 'false');
    return !bad;
  }
  function validate() {
    var ok = true;
    var name = form.from_name, mail = form.reply_to, msg = form.message;
    ok = flag(name, !name.value.trim()) && ok;
    ok = flag(mail, !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(mail.value.trim())) && ok;
    ok = flag(msg, !msg.value.trim()) && ok;
    return ok;
  }

  ['from_name', 'reply_to', 'message'].forEach(function (n) {
    form[n].addEventListener('input', function () {
      if (form[n].closest('.field').classList.contains('err')) validate();
    });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (form.website.value) return;               // honeypot
    if (!validate()) {
      say('bad', 'A couple of fields still need you.');
      form.querySelector('.field.err input, .field.err textarea').focus();
      return;
    }
    var configured = CFG.publicKey.indexOf('EMAILJS_') !== 0;
    if (!configured || typeof emailjs === 'undefined') {
      say('bad', 'The form isn\'t connected yet. For now, email lisa@brilliantlysane.org or call 970-368-9185.');
      return;
    }
    btn.disabled = true;
    btn.textContent = 'Sending';
    say('ok', 'Sending.');
    emailjs.init({ publicKey: CFG.publicKey });
    emailjs.sendForm(CFG.serviceId, CFG.templateId, form).then(function () {
      form.reset();
      btn.textContent = 'Sent';
      say('ok', 'That reached me. I answer these myself, usually within two business days.');
    }).catch(function () {
      btn.disabled = false;
      btn.textContent = 'Send it';
      say('bad', 'Something went wrong on my end. Please email lisa@brilliantlysane.org or call 970-368-9185.');
    });
  });
})();
