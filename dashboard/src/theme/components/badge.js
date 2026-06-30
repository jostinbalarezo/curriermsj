import { mode } from "@chakra-ui/theme-tools"

export const badgeStyles = {
  components: {
    Badge: {
      baseStyle: {
        borderRadius: "10px",
        letterSpacing: "0px",
        fontWeight: "700",
        fontSize: "10px",
      },
      variants: {
        brand: (props) => ({
          bg: mode("brand.500", "brand.400")(props),
          color: "white",
        }),
        outline: (props) => ({
          bg: "transparent",
          color: mode("secondaryGray.500", "white")(props),
          border: "1px solid",
          borderColor: mode("secondaryGray.500", "white")(props),
        }),
      },
    },
  },
}
