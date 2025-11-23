import { Link, useLocation } from "react-router-dom";
import { ReactNode } from "react";

const navItems = [
  { path: "/sectors", label: "섹터" },
  { path: "/indicators", label: "지표" },
  { path: "/keywords", label: "키워드" }
];

interface Props {
  children: ReactNode;
}

function Layout({ children }: Props) {
  const location = useLocation();

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <h1>Stock Analytics</h1>
        <nav>
          {navItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className={location.pathname.startsWith(item.path) ? "active" : ""}
            >
              {item.label}
            </Link>
          ))}
        </nav>
      </aside>
      <main className="content">{children}</main>
    </div>
  );
}

export default Layout;

