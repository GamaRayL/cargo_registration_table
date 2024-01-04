import axios from "axios";
import {API_URL} from "@/constants";

export function pathArrival(data) {
    return axios.patch(`${API_URL}/posts`, data)
}