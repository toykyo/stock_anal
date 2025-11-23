import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";

import MetricCard from "../components/MetricCard";
import { fetchDailyPrices, fetchSymbol } from "../api/client";

function SymbolDetail() {
  const params = useParams<{ symbolId: string }>();
  const symbolId = Number(params.symbolId);

  const symbolQuery = useQuery({
    queryKey: ["symbol", symbolId],
    queryFn: () => fetchSymbol(symbolId),
    enabled: Number.isFinite(symbolId)
  });

  const pricesQuery = useQuery({
    queryKey: ["prices", symbolId],
    queryFn: () => fetchDailyPrices(symbolId),
    enabled: Number.isFinite(symbolId)
  });

  if (!Number.isFinite(symbolId)) {
    return <div>잘못된 종목입니다.</div>;
  }

  if (symbolQuery.isLoading || pricesQuery.isLoading) {
    return <div>로딩중...</div>;
  }

  const symbol = symbolQuery.data?.data;
  const prices = pricesQuery.data?.data ?? [];

  return (
    <div className="page">
      <header>
        <h2>{symbol?.name}</h2>
        <p>{symbol?.ticker}</p>
      </header>
      <section className="grid">
        {prices.slice(0, 4).map((price) => (
          <MetricCard
            key={price.id}
            title={price.trade_date}
            value={`${price.close.toLocaleString()} ₩`}
            delta={price.close_delta}
            subtitle={`거래량 ${price.volume?.toLocaleString() ?? "-"} / 외국인 ${
              price.foreign_net ?? "-"
            }`}
          />
        ))}
      </section>
    </div>
  );
}

export default SymbolDetail;

