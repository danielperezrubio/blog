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
            href="https://www.facebook.com/daniel.perezrubio.75033/"
            target="_blank"
            className="me-3"
          >
            <i className="bi bi-facebook"></i>
          </a>
          <a
            href="https://www.linkedin.com/in/danielperezrubio/"
            target="_blank"
          >
            <i className="bi bi-linkedin"></i>
          </a>
        </section>
      </div>
    </footer>
  );
}

export default Footer;
