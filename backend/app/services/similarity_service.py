from app.models.jewel import JewelRequest


class SimilarityService:

    def compare(self, target: JewelRequest, candidate: JewelRequest):
        target_ids = {attr.id for attr in target.attributes if attr.id}
        candidate_ids = {attr.id for attr in candidate.attributes if attr.id}

        if not target_ids:
            return 0.0

        matching_ids = target_ids.intersection(candidate_ids)

        similarity = len(matching_ids) / len(target_ids)

        return round(similarity, 2)


similarity_service = SimilarityService()