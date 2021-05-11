/** @format */

import { useEffect, useState } from "react";
export default function useFetchData({ url, data, needsFetch }) {
  const [response, setResponse] = useState();
  const [errors, setErrors] = useState();
  useEffect(() => {
    let opts = { body: JSON.stringify(data), mode: "cors", method: "POST" };
    async function fetchData() {
      try {
        const resp = await (await fetch(url, opts)).json();
        setResponse(resp);
      } catch (err) {
        setErrors(err);
      }
    }
    if (needsFetch) {
      fetchData();
    }
  }, [needsFetch, setResponse, setErrors, options]);
  return { response: response, errors: errors };
}
