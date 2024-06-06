

export default eventHandler(async (event) => {
    const body = await readBody(event)
    const resume = body.resume._value
    const resp = await $fetch("http://127.0.0.1:8000/extract", { body: { "resume": resume }, method: "POST" })
    return resp
})