import "./Footer.css";

function Footer() {
  return (
    <footer id="footer">
      <div className="container">
        <div className="me-auto text-muted">
          <span>© 2023 Daniel Pérez Rubio</span>
        </div>
        <section>
          <a
            href="https://www.linkedin.com/in/danielperezrubio/"
            target="_blank"
            rel="noreferrer"
          >
            <i className="bi bi-linkedin"></i>
          </a>
        </section>
      </div>
    </footer>
  );
}

export default Footer;
