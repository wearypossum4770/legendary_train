/** @format */

import PostList from "./PostList";
import Repository from "./Repository";
import { NewsRepository } from "./NewsRepository";
class __PostNotFoundException__ extends Error {
  constructor(postId) {
    super(`Post with id ${postId} not found`);
  }
}
const PostNotFoundException = message => new __PostNotFoundException__(message);

let postsRepository = {
  findOne: function (_id) {
    return this.repository.filter(post => post.id === _id)[0];
  },
  rawRepository: NewsRepository,
  get repository() {
    return this.rawRepository[0]["data"];
  },
};

async function getPostById(_id) {
  //PostNotFoundException
  const post = await postsRepository.find(_id);
  if (post) {
    return post;
  }
  throw PostNotFoundException(_id);
}
export default function Blog() {
  //http://api.mediastack.com/v1/news?access_key=4cebe094d8cb2e950c166b192021a5c6&sources=cnn
  return (
    <div>
      <PostList post_list={postsRepository.repository} />
    </div>
  );
}
