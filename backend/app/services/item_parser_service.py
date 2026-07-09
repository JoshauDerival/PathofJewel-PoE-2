from app.models.jewel import JewelRequest, JewelAttribute


class ItemParserService:

    def parse_jewel_text(self, item_text: str) -> JewelRequest:
        lines = [
            line.strip()
            for line in item_text.splitlines()
            if line.strip() and line.strip() != "--------"
        ]

        base_type = "Unknown Jewel"
        item_level = 0
        attributes = []

        for line in lines:
            if line.startswith("Item Level:"):
                item_level = int(line.replace("Item Level:", "").strip())

            elif "%" in line or "+" in line:
                attributes.append(
                    JewelAttribute(
                        name=line,
                        value=self.extract_first_number(line),
                        type="explicit"
                    )
                )

            elif "Jewel" in line:
                base_type = line

        return JewelRequest(
            base_type=base_type,
            item_level=item_level,
            attributes=attributes
        )

    def extract_first_number(self, text: str) -> float:
        current = ""

        for char in text:
            if char.isdigit() or char == ".":
                current += char
            elif current:
                break

        if current:
            return float(current)

        return 0.0


item_parser_service = ItemParserService()