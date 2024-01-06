import axios from "axios";
import {API_URL} from "../constants.js";

export function pathShipment(data) {
    return axios.patch(`${API_URL}/shipments/`, data)
}

export async function getShipmentList() {

    const response = await axios.get(`${API_URL}/shipments/`);
    return response.data
}