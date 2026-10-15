document.addEventListener('DOMContentLoaded', () => {
  // Hamburger Menu Toggle
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('nav-links');

  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      navLinks.classList.toggle('active');
    });
  }

  // Scroll Animations using IntersectionObserver
  const fadeElements = document.querySelectorAll('.fade-in, .slide-up');
  
  const appearOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
  };

  const appearOnScroll = new IntersectionObserver(function(entries, observer) {
    entries.forEach(entry => {
      if (!entry.isIntersecting) {
        return;
      } else {
        entry.target.classList.add('appear');
        observer.unobserve(entry.target);
      }
    });
  }, appearOptions);

  fadeElements.forEach(el => {
    appearOnScroll.observe(el);
  });

  // Contact Form Submission Handler (All Student Executive Board Members in One Email, Excluding Faculty Advisor)
  const EXEC_BOARD_EMAILS = "cozeir@my.okcu.edu,jacob.beckham@my.okcu.edu,hbergmannbusby@my.okcu.edu,dadamez@my.okcu.edu,kristyn.hart@my.okcu.edu";

  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const nameInput = document.getElementById('name');
      const emailInput = document.getElementById('email');
      const messageInput = document.getElementById('message');

      const name = nameInput ? nameInput.value.trim() : 'Website Visitor';
      const email = emailInput ? emailInput.value.trim() : '';
      const message = messageInput ? messageInput.value.trim() : '';
      const currentDate = new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' });

      const emailSubject = encodeURIComponent(`[IPLS Website Contact] Message from ${name}`);
      const emailBody = 
`IPLS CONTACT FORM MESSAGE
==================================================
Date: ${currentDate}
From: ${name}
Sender Email: ${email}

MESSAGE:
--------------------------------------------------
${message}

--------------------------------------------------
Executive Board Recipients Included:
- cozeir@my.okcu.edu (Cloudia Ozeir, Co-President)
- jacob.beckham@my.okcu.edu (Jacob Beckham, Co-President)
- hbergmannbusby@my.okcu.edu (Helene Bergmann-Busby, Vice President)
- dadamez@my.okcu.edu (Danyelle Adamez, Treasurer)
- kristyn.hart@my.okcu.edu (Kristyn M. Hart, Secretary)
==================================================`;

      const mailtoUrl = `mailto:${EXEC_BOARD_EMAILS}?cc=${encodeURIComponent(email)}&subject=${emailSubject}&body=${encodeURIComponent(emailBody)}`;

      // Show confirmation alert
      alert(`Thank you, ${name}! Your message is being sent to the IPLS Executive Board (Cloudia, Jacob, Helene, Danyelle, and Kristyn).`);

      // Launch mail client pre-addressed to all 5 student board members
      window.location.href = mailtoUrl;

      contactForm.reset();
    });
  }

  // Newsletter Form Submission Handler
  const newsletterForm = document.getElementById('newsletterForm');
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Thanks for subscribing to our newsletter!');
      newsletterForm.reset();
    });
  }
});
