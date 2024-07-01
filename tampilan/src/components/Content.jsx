import React, { useEffect, useState } from 'react';

function Content() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/posts/')
      .then(response => response.json())
      .then(data => setPosts(data))
      .catch(error => console.error('Error fetching posts:', error));
  }, []);

  return (
    <div className="container">
      <div className="row">
        <div className="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
          {posts.map(post => (
            <div className="post-preview" key={post.id}>
              <a href={`post/${post.id}.html`}>
                <h2 className="post-title">{post.title}</h2>
                <h3 className="post-subtitle">{post.content}</h3>
              </a>
              <p className="post-meta">
                Posted on {new Date(post.created_at).toLocaleDateString()}
              </p>
              <hr />
            </div>
          ))}
          {/* Pager */}
          <ul className="pager">
            <li className="next">
              <a href="#">Older Posts &rarr;</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Content;
