import axios from "axios";

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL ?? "/api/v1",
  timeout: 10000
});

export interface Sector {
  id: number;
  name: string;
  description?: string;
  market?: string;
}

export interface Symbol {
  id: number;
  ticker: string;
  name: string;
  market?: string;
  sector_id?: number;
}

export interface Indicator {
  id: number;
  code: string;
  name: string;
  frequency?: string;
  description?: string;
}

export interface DailyPrice {
  id: number;
  symbol_id: number;
  trade_date: string;
  close: number;
  close_delta?: number;
  volume?: number;
  foreign_net?: number;
  institutional_net?: number;
  individual_net?: number;
}

export const fetchSectors = () => apiClient.get<Sector[]>("/sectors");
export const fetchSymbols = () => apiClient.get<Symbol[]>("/symbols");
export const fetchSymbol = (symbolId: number) =>
  apiClient.get<Symbol>(`/symbols/${symbolId}`);
export const fetchIndicators = () => apiClient.get<Indicator[]>("/indicators");
export const fetchDailyPrices = (symbolId?: number) =>
  apiClient.get<DailyPrice[]>("/prices", { params: { symbol_id: symbolId } });
