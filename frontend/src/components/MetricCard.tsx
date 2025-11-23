import { ReactNode } from "react";

interface MetricCardProps {
  title: string;
  value: ReactNode;
  delta?: number;
  subtitle?: string;
}

function MetricCard({ title, value, delta, subtitle }: MetricCardProps) {
  return (
    <div className="metric-card">
      <div className="metric-title">{title}</div>
      <div className="metric-value">{value}</div>
      {typeof delta === "number" && (
        <div className={`metric-delta ${delta >= 0 ? "up" : "down"}`}>
          {delta >= 0 ? "+" : ""}
          {delta?.toFixed(2)}
        </div>
      )}
      {subtitle && <div className="metric-subtitle">{subtitle}</div>}
    </div>
  );
}

export default MetricCard;

