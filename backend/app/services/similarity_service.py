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
    
    def compare_listing(self, target_ids, listing):

        listing_ids = set(listing["attributes"])

        if not target_ids:
            return 0

        matches = target_ids.intersection(listing_ids)

        return len(matches) / len(target_ids)


similarity_service = SimilarityService()