/** @format */
// ["author", "title", "description", "url", "source", "image", "category", "language", "country", "published_at"]
import { useHistory } from "react-router-dom";

export default function PostList({ post_list }) {
  let history = useHistory();
  const navigateToPosting = _id => history.push(`/blog/${_id}`);
  return post_list.map((post, index) => (
    <div onClick={e => navigateToPosting(index)} key={index}>
      <div className="w3-card-4">
        <header className="w3-container w3-blue">
          <h1>{post.title}</h1>
        </header>
        <div className="w3-container w3-center">
          <br />
          <img src={post.image} alt="Avatar" style={{ width: "80%" }} />
        </div>
        <div className="w3-container">
          <p>{post.description}</p>
        </div>
        <footer className="w3-container w3-blue">
          <h5>{`source:${post.source}\nPublished: ${new Date(
            post.published_at,
          ).toLocaleDateString()}`}</h5>
        </footer>
      </div>
    </div>
  ));
}
