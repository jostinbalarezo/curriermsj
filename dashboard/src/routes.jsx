import React from "react"
import { Icon } from "@chakra-ui/react"
import { MdHome, MdPeople, MdSchedule, MdWarning, MdSecurity } from "react-icons/md"
import MainDashboard from "views/admin/default"
import ObservabilityDashboard from "views/admin/observability"
import ClientesDashboard from "views/admin/clientes"
import PendientesDashboard from "views/admin/pendientes"
import ReportesDashboard from "views/admin/reportes"

const routes = [
  {
    name: "Main Dashboard",
    layout: "/admin",
    path: "/default",
    icon: <Icon as={MdHome} width="20px" height="20px" color="inherit" />,
    component: <MainDashboard />,
  },
  {
    name: "Clientes",
    layout: "/admin",
    path: "/clientes",
    icon: <Icon as={MdPeople} width="20px" height="20px" color="inherit" />,
    component: <ClientesDashboard />,
  },
  {
    name: "Envíos",
    layout: "/admin",
    path: "/pendientes",
    icon: <Icon as={MdSchedule} width="20px" height="20px" color="inherit" />,
    component: <PendientesDashboard />,
  },
  {
    name: "Reportes",
    layout: "/admin",
    path: "/reportes",
    icon: <Icon as={MdWarning} width="20px" height="20px" color="inherit" />,
    component: <ReportesDashboard />,
  },
  {
    name: "Observabilidad",
    layout: "/admin",
    path: "/observability",
    icon: <Icon as={MdSecurity} width="20px" height="20px" color="inherit" />,
    component: <ObservabilityDashboard />,
  },
]

export default routes
