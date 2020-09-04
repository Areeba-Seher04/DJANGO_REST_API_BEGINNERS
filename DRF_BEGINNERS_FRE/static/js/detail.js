
// it will catch the id from url
console.log(window.location.pathname)
const pathname = window.location.pathname
const pathnameParts = pathname.split('/')
const postID = pathnameParts[pathnameParts.length -2 ];
console.log(postID)

function getPost(postID) {
	fetch(`/api/posts/${postID}/`)
	.then(res => res.json())
	.then(data => {
		console.log(data)
	})
	.catch(err => {
		console.error(err);
	})
}

getPost(postID);

function deletePost(postID) {
	const data = {
		method : "DELETE",
		headers : {
			'Content-Type' : 'application/json'
		}
	}
	fetch(`/api/posts/${postID}/delete/`, data)
	.then(() => {
		console.log('redirect')
	})
	.catch(err => {
		console.error(err);
	})
}

deletePost(1)