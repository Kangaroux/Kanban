export default {
  formError(err) {
    const data = err.response.data;

    // If no status was included something is wrong with the server
    if(data.status == null) {
      return {
        formError: "An unexpected error occurred.",
        fieldErrors: {}
      };
    }

    return {
      formError: data.msg,
      fieldErrors: data.fields || {}
    };
  }
};