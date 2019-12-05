from datetime import datetime, timezone

from django.core.management.base import BaseCommand, CommandError

from website import models


class Command(BaseCommand):
    help = 'This command finds all the closed auctions and assigns each auction a winnning bid id'

    def handle(self, *args, **options):
        """
        This function closes any auctions that need to be closed. it does this by the following

        1. get all the auction objects
        2. filter auction object by those where the system time > auction close time
        3. for all auction objects, obtain their id
        4. filter bids by auction id and sort by highest bid first
        4a. if auction has no bids, then close
        5. if auction has bid and highest bid obtained, close bid and in auction object assign the winning bid
        """

        # get all auction objects
        all_auction = models.Auction.objects.all()

        # if there are not auction available, do nothing
        if all_auction.count() == 0:
            return

        # loop through all auctions
        for i in all_auction:
            # get all the bids beloning to a specigic auction
            bids = models.Bid.objects.filter(auctionid_id=i.id)

            # check if the auction is closed by comparing current time against
            # auction closed time

            if i.auctionCloseTimestamp > datetime.now(timezone.utc):
                continue

            # check if that specific auction has a bid
            if bids.count() == 0:
                pass
            else:
                highestBid = bids.order_by('-amount')[0]
                i.winningBid = highestBid

            i.auctionOpen = False
            i.save()
