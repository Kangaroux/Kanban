import Axios from "axios";
import Promise from "promise";
import Qs from "qs";


export function registerUser(data) {
  return new Promise((resolve, reject) => {
    Axios.post(api.user, Qs.stringify(data))
      .then((resp) => {
        resolve(resp.data.user);
      })
      .catch((err) => {
        reject(err.response.data);
      });
  });
}