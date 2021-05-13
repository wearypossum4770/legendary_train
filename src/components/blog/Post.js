/** @format */
import { NewsRepository } from "./NewsRepository";
import { useParams } from "react-router-dom";
export default function Post(props) {
  let { post_id } = useParams();
  let post = NewsRepository[0]["data"][post_id];
  return (
    <div className="w3-card-4">
      <header className="w3-container w3-light-gray">
        <h1>{post.title}</h1>
      </header>
      <div className="w3-container w3-center">
        <br />
        <h2>
          <a href={post.url}>
            Read full story here...
            <span className="sr-only">opens link to news article</span>{" "}
            <i aria-hidden="true" className="fa fa-edit fa-external-link"></i>
          </a>
        </h2>
        <br />
        <img
          loading="lazy"
          src={post.image}
          alt="Avatar"
          style={{ width: "80%" }}
        />
      </div>
      <div className="w3-container">
        <p>{post.description}</p>
      </div>
      <footer className="w3-container w3-light-gray">
        <h5>{`Author: ${post.author ?? "No Author listed"}`}</h5>
        <h5>{`News Source:\t${post.source}`}</h5>
        <h5>{`Originally Published: ${new Date(
          post.published_at,
        ).toLocaleDateString()}`}</h5>
      </footer>
    </div>
  );
}
