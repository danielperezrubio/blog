import PostRecentList from "../components/PostRecentList";

function Home() {
  return (
    <div className="container mt-3">
      <h1>Welcome to Daniel's Programming Blog!</h1>
      <p>
        I'm a passionate programmer with a strong focus on web development and
        software engineering. This blog is a collection of my programming
        knowledge, tips, and experiences. It serves as personal reference for me
        to revisit whenever I need a quick reminder on a particular topic.
      </p>
      <p>
        Feel free to explore the various posts on my blog and don't hesitate to
        reach out if you have any questions or feedback. Happy coding!
      </p>
      <PostRecentList />
    </div>
  );
}

export default Home;
