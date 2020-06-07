const axios = require('axios')
const fs = require('fs')

const ID_POST = ''
const ACCESS_TOKEN = ''

const renderMsg = cmtObj => {
	if(cmtObj.message && cmtObj.attachment) {
		return `${cmtObj.message}\n    *${cmtObj.attachment.type.toUpperCase()}* - ${cmtObj.attachment.media.image.src}`
	} else if(cmtObj.attachment) {
		return `*${cmtObj.attachment.type.toUpperCase()}* - ${cmtObj.attachment.media.image.src}`
	} else {
		return `${cmtObj.message}`
	}
}

const writeFile = async (id, token) => {
	const response = await axios.get(`https://graph.facebook.com/v3.1/${id}?fields=comments.limit(10000){comments.limit(1000){message,from,attachment},message,from,attachment}&access_token=${token}`)
	const { data: { comments: { data } } } = response

	const prevId = []
	const cmtFormatted = data.reduce((accumulator, currentCmt) => {
		if(prevId.includes(currentCmt.id)) return accumulator

		accumulator += `u/${currentCmt.from.name}: ${renderMsg(currentCmt)}\n`

		if(currentCmt.hasOwnProperty('comments')) {
			currentCmt.comments.data.forEach(comment => {
				prevId.push(comment.id)
				accumulator += ` > u/${comment.from.name}: ${renderMsg(comment)}\n`
			})
		}

		return accumulator
	}, '')

	fs.writeFile(`${id}.txt`, cmtFormatted, () => {
		console.log('xong')
	})
}

writeFile(ID_POST, ACCESS_TOKEN)
